import shortuuid
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import ContactForm, BuyForm
from .models import Client

inner_menu = [{'title':"Главная", 'url_name':'main-page'},
            {'title':"Абонементы", 'url_name':'abonements'},
            {'title':"Услуги", 'url_name':'services'},
            {'title':"Галерея", 'url_name':'gallery'},
            {'title':"Тренеры", 'url_name':'trainers'},
            {'title':"Сертификаты", 'url_name':'sertificates'},
            {'title':"Контакты", 'url_name':'contacts'},
        ]
menu = [{'title':"Абонементы", 'url_name':'abonements'},
        {'title':"Услуги", 'url_name':'services'},
        {'title':"Галерея", 'url_name':'gallery'},
        {'title':"Тренеры", 'url_name':'trainers'},
        {'title':"Сертификаты", 'url_name':'sertificates'},
        {'title':"Контакты", 'url_name':'contacts'},
        ]

sub_item_1 = [ {'subscription_heading':" “Начальный” ",
              'subscription_lead':"Если вы начинающий спортсмен, рекомендуем начать с самого первого абонемента. Когда вы освоитесь у нас в спортивном комплексе - можно будет сделать обновление. Базовые функции клуба к вашим услугам.",
              'sub_item_1':"Абонемент на 12 месяцев",'sub_item_2':"2 консультации тренера фитнес-клуба",'sub_item_3':"Личный шкафчик",
              'sub_item_4':"Доступ к солярию бесплатно(1 месяц)",'sub_item_5':"Консультация в салоне красоты",'sub_item_6':"Консультация у диетолога",
              'sub_info_1':"18 000 ",'sub_info_2':"12 ",'value':"Начальный"},
            ]


sub_item_2 =[{'subscription_heading':" “Любитель” ",
                'subscription_lead':"Стандартный вид абонемента, который позволит вам полностью воспользоваться улслугами нашего фитнес-клуба. К вашему распоряжениию работа с тренером, диетологом и косметологом. Получите максимум результата.",
                'sub_item_1':"Абонемент на 12 месяцев",'sub_item_2':"4 консультации тренера фитнес-клуба",'sub_item_3':"Личный шкафчик",'sub_item_4':"Доступ к солярию бесплатно(3 месяца)",'sub_item_5':"2 консультации у диетолога",'sub_item_6':"3 услуги салона красоты",'sub_info_1':"27 000 ",'sub_info_2':"12 ",'value':"Любитель"},
            ]


sub_item_3=[{'subscription_heading':" “Профессионал” ",
                'subscription_lead':"Для тех, кто очень серьезно подходит к процессу тренировок. Мы поможем вам достигнуть максимальных результатов в спорте. Для вашего результата мы подключили: личного тренера, диетолога, косметолога. Достигнем результата вместе!",
                'subscription_image':"/static/img/src/professional.jpg",
                'sub_item_1':"Абонемент на 12 месяцев",'sub_item_2':"35 консультации тренера фитнес-клуба",'sub_item_3':"Личный шкафчик",'sub_item_4':"Доступ к солярию бесплатно(12 месяцев)",'sub_item_5':"8 консультаций диетолога",'sub_item_6':"20 услуг салона красоты",'sub_info_1':"90 000 ",'sub_info_2':"12 ",'value':"Профессионал"},]

def index(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      data={
        'name':form.cleaned_data['name'],
        'phone':form.cleaned_data['phone'],
        'message':form.cleaned_data['message'],
        'subject':'Обратная связь'
      }
      html_body = render_to_string("../templates/main/temp_email.html", data)
      msg = EmailMultiAlternatives(subject='Обратная связь', to=['solodow.mitya@yandex.by'])
      msg.attach_alternative(html_body,"text/html")
      msg.send()
      messages.success(request,'Success! Ваше письмо отправлено!')
    else:
      messages.error(request,"Error! Ваше письмо не отправлено!")
  form = ContactForm()
  return render(request, 'main/main-page.html', {'menu': menu,"form":form})


def abonements(request):
    if request.method == 'POST':
        buyform = BuyForm(request.POST)
        form = ContactForm(request.POST)
        indicator = 0
        if buyform.is_valid():
            unikID = shortuuid.ShortUUID().random(length=8)
            data = {
                'name': buyform.cleaned_data['name'],
                'phone': buyform.cleaned_data['phone'],
                'email': buyform.cleaned_data['email'],
                'hidden':buyform.cleaned_data['hidden'],
                'unikID': unikID
            }
            useremail = buyform.cleaned_data['email']
            html_body = render_to_string("../templates/parts/temp_abon.html", data)
            msg = EmailMultiAlternatives(subject='Информация о вашем абонементе', to=[useremail])
            msg.attach_alternative(html_body, "text/html")
            msg.send()
            Client.objects.create(name=buyform.cleaned_data['name'],phone=buyform.cleaned_data['phone'],unikID=unikID,subscription=buyform.cleaned_data['hidden'])
            messages.success(request, 'Success! Ваш заказ принят!')

        else:
            if form.is_valid():
                indicator = 0
            else:
               if indicator != 1:
                  messages.error(request, "Error! Ваш заказ не принят!")
            indicator = 1

        if form.is_valid():
            subject = 'Консультация'
            data = {
                'name': form.cleaned_data['name'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
                'subject':subject
            }
            html_body = render_to_string("../templates/main/temp_email.html", data)
            msg = EmailMultiAlternatives(subject='Консультация', to=['solodow.mitya@yandex.by'])
            msg.attach_alternative(html_body, "text/html")
            msg.send()
            messages.success(request, 'Success! Ваше письмо отправлено!')
        else:
            if buyform.is_valid():
                indicator = 1
            else:
                if indicator !=1:
                 messages.error(request, "Error! Ваше письмо не отправлено!")

    form = ContactForm()
    buyform = BuyForm()
    return render(request,'main/abonements.html',{"form":form,"buyform": buyform,'inner_menu':inner_menu,'menu': menu,'sub_item_1':sub_item_1,'sub_item_2':sub_item_2,'sub_item_3':sub_item_3})

def services(request):
  return render(request, 'main/services.html',{'inner_menu':inner_menu,'menu': menu})


def trainers(request):
  return render(request, 'main/trainers.html',{'inner_menu':inner_menu,'menu': menu})


def sertificates(request):
  return render(request, 'main/sertificates.html',{'inner_menu':inner_menu,'menu': menu})


def gallery(request):
  return render(request, 'main/gallery.html',{'inner_menu':inner_menu,'menu': menu})


def contacts(request):
  return render(request, 'main/contacts.html',{'inner_menu':inner_menu,'menu': menu})


def forum(request):
  return render(request, 'main/forum.html',{'inner_menu':inner_menu,'menu': menu})