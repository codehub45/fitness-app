import json
from django.http import JsonResponse
from fitness.models import Classes,Slots,Bookings
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.db.models import F


# Get the class
@csrf_exempt
def get_class(request):
    if request.method == "GET":
        slot_list = (Slots.objects.annotate(class_name=F('classes__class_name'),instructor=F('classes__instructor')).
                     values('class_name','classes_id','slots','start_timings','end_timings','instructor'))
        slot_dict = dict()
        for slot in slot_list:
            slot_data = {'classes_id':slot['classes_id'],'slots':slot['slots'],'timing':str(slot['start_timings']) + '-' + str(slot['end_timings']),'instructor':slot['instructor']}
            if slot['class_name'] in slot_dict:
                slot_dict[slot['class_name']].append(slot_data)
            else:
                slot_dict[slot['class_name']] = [slot_data]
        return JsonResponse(slot_dict, safe=False)

#Master Create Classess
@csrf_exempt
def create_class(request):
    if request.method == "POST":
        Classes.objects.all().delete()  # Delete all rows
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='fitness_classess'")
        dict_data = json.loads(request.body)
        class_list = list()
        for i in dict_data:
            class_object = Classes(class_name=i['class_name'],instructor=i['instructor'])
            class_list.append(class_object)
        Classes.objects.bulk_create(class_list)
        return JsonResponse({"Message":'success'}, safe=False)
    else:
        return JsonResponse({"Message":'Method now Allowed'}, safe=False)

@csrf_exempt
def create_slots(request):
    if request.method == "POST":
        dict_data = json.loads(request.body)
        slot_list = list()
        for i in dict_data:
            slot_object = Slots(classes=Classes.objects.get(id=i['class_id']),start_timings=i['start_timings'],slots=i['slot'],end_timings=i['end_timings'])
            slot_list.append(slot_object)
        Slots.objects.bulk_create(slot_list)
        return JsonResponse({"Message": 'success'}, safe=False)
    else:
        return JsonResponse({"Message": 'Method now Allowed'}, safe=False)

@csrf_exempt
def book_class(request):
    if request.method == "POST":
        dict_data = json.loads(request.body)
        class_id = dict_data['class_id']
        client_name= dict_data['client_name']
        client_email = dict_data['client_email']
        slot = dict_data['slot']
        date = dict_data['date']
        error_msg = {"error":"Invalid Data"}
        for i in dict_data.keys():
            if dict_data.get(i) is None or dict_data.get(i) == "":
                return JsonResponse(error_msg, safe=False)

        bookingss = Bookings.objects.filter(client_email=client_email,class_id=class_id,date_time=date,slots=slot)
        if bookingss:
            return JsonResponse({"error": "Slot Already Booked"}, safe=False)

        classes = Classes.objects.get(id=class_id)
        slots = Slots.objects.filter(slots=slot,classes=classes)
        if not classes or not slots:
            if not slots:
                return JsonResponse({"error": "Timings not Available"}, safe=False)
            return JsonResponse(error_msg, safe=False)

        Bookings.objects.create(client_name=client_name,client_email=client_email,class_id=classes,date_time=date,slots=slots[0])
        return JsonResponse({"Message": 'success'}, safe=False)


def get_bookings(request):
    if request.method == "GET":
        email = request.GET.get('email')
        if email is None or email == "":
            return JsonResponse({"error":"Invalid Data"}, safe=False)

        book_details = Bookings.objects.filter(client_email=email)
        book_details_dict = dict()
        if book_details.count() != 0:
            for i in book_details:
                book_details_dict['client_name'] = i.client_name
                book_details_dict['client_email'] = i.client_email
                classes_dict = {"class_id":i.class_id.id,"class_name":i.class_id.class_name, "instructor":i.class_id.instructor,"slot_timing":str(i.slots.start_timings) + "-" + str(i.slots.end_timings),'date':str(i.date_time)}
                if 'classes' not in book_details_dict:
                    book_details_dict['classes'] = [classes_dict]
                else:
                    book_details_dict['classes'].append(classes_dict)

        return JsonResponse(book_details_dict, safe=False)

