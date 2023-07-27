from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.template import loader
from .models import *
from .models import reserve

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def Helpcentre(request):
    template = loader.get_template('Helpcentre.html')
    return HttpResponse(template.render())

def cancellation(request):
    template = loader.get_template('cancellation.html')
    return HttpResponse(template.render())

def termsandconditions(request):
    template = loader.get_template('termsandconditions.html')
    return HttpResponse(template.render())

def Howwework(request):
    template = loader.get_template('Howwework.html')
    return HttpResponse(template.render())

def reservesuccess(request):
    template = loader.get_template('reservesuccess.html')
    return HttpResponse(template.render())


def reserves(request,pname):
    if(Folvika.objects.filter(name=pname)):
        plm=Folvika.objects.filter(name=pname).first()
        return render(request,"reserveform.html",{"Folvikas":plm})
    else:
        return redirect('/')   

def addData(request):
    if request.method=="POST":
        hotelname=request.POST["hotelname"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        mail=request.POST["mail"]
        mobile=request.POST["mobile"]
        country=request.POST["country"]
        guest=request.POST["guest"]
        from_date=request.POST["from_date"]
        to_date=request.POST["to_date"]

        obj=reserve()
        obj.Hotelname=hotelname
        obj.Firstname=firstname
        obj.Lastname=lastname
        obj.Mail=mail
        obj.Mobile=mobile
        obj.Country=country
        obj.Guest=guest
        obj.From_date=from_date
        obj.To_date=to_date
        obj.save()
        mydata=reserve.objects.all()
        return redirect("home")
    return render(request,"reserveform.html")

def reserveforms(request):
    template = loader.get_template('reserveforms.html')
    return HttpResponse(template.render())


def addDatas(request):
    if request.method=="POST":
        hotelname=request.POST["hotelname"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        mail=request.POST["mail"]
        mobile=request.POST["mobile"]
        country=request.POST["country"]
        guest=request.POST["guest"]
        from_date=request.POST["from_date"]
        to_date=request.POST["to_date"]

        obj=reserves()
        obj.Hotelname=hotelname
        obj.Firstname=firstname
        obj.Lastname=lastname
        obj.Mail=mail
        obj.Mobile=mobile
        obj.Country=country
        obj.Guest=guest
        obj.From_date=from_date
        obj.To_date=to_date
        obj.save()
        mydata=reserves.objects.all()
        return redirect("home")
    return render(request,"reserveforms.html")


def allarctic(request):
    template = loader.get_template('allarctic.html')
    return HttpResponse(template.render())

def alldesign(request):
    template = loader.get_template('alldesign.html')
    return HttpResponse(template.render())

def allfarms(request):
    template = loader.get_template('allfarms.html')
    return HttpResponse(template.render())

def allisland(request):
    template = loader.get_template('allisland.html')
    return HttpResponse(template.render())

def alltinyhome(request):
    template = loader.get_template('alltinyhome.html')
    return HttpResponse(template.render())

def alltopofworld(request):
    template = loader.get_template('alltopofworld.html')
    return HttpResponse(template.render())



def FolvikaEye(request):
    folvikas=Folvika.objects.all
    template = loader.get_template('FolvikaEye.html')
    return render(request,"FolvikaEye.html",{"Folvikas":folvikas})



def Hillagammi(request):
    template = loader.get_template('Hillagammi.html')
    return HttpResponse(template.render())

def TheArcticHideaway(request):
    template = loader.get_template('TheArcticHideaway.html')
    return HttpResponse(template.render())

def StraumenSeaViewMagicArcticGetaway(request):
    template = loader.get_template('StraumenSeaViewMagicArcticGetaway.html')
    return HttpResponse(template.render())

def OlleroEcoLodge(request):
    template = loader.get_template('OlleroEcoLodge.html')
    return HttpResponse(template.render())

def HuskyDreamsTipi(request):
    template = loader.get_template('HuskyDreamsTipi.html')
    return HttpResponse(template.render())

def Aurahouse(request):
    template = loader.get_template('Aurahouse.html')
    return HttpResponse(template.render())

def IKSHAA(request):
    template = loader.get_template('IKSHAA.html')
    return HttpResponse(template.render())

def JimmysVilla4BHKwPoolAssagaonAnjuna(request):
    template = loader.get_template('JimmysVilla4BHKwPoolAssagaonAnjuna.html')
    return HttpResponse(template.render())

def LaZamoravilla(request):
    template = loader.get_template('LaZamoravilla.html')
    return HttpResponse(template.render())

def MarbleSunvilla(request):
    template = loader.get_template('MarbleSunvilla.html')
    return HttpResponse(template.render())

def VillaPadma(request):
    template = loader.get_template('VillaPadma.html')
    return HttpResponse(template.render())

def FlowerValleyPlantation(request):
    template = loader.get_template('FlowerValleyPlantation.html')
    return HttpResponse(template.render())

def FootprintWildernessExperience(request):
    template = loader.get_template('FootprintWildernessExperience.html')
    return HttpResponse(template.render())

def LalaLandFarmResort(request):
    template = loader.get_template('LalaLandFarmResort.html')
    return HttpResponse(template.render())

def SerenityHomestay(request):
    template = loader.get_template('SerenityHomestay.html')
    return HttpResponse(template.render())
    
def VanandhaaraCoorg(request):
    template = loader.get_template('VanandhaaraCoorg.html')
    return HttpResponse(template.render())

def WhisperingWatersArtistCottage(request):
    template = loader.get_template('WhisperingWatersArtistCottage.html')
    return HttpResponse(template.render())

def BeautifulOceanfrontCabana(request):
    template = loader.get_template('BeautifulOceanfrontCabana.html')
    return HttpResponse(template.render())

def cubacali(request):
    template = loader.get_template('cubacali.html')
    return HttpResponse(template.render())

def DriftwoodMentawai(request):
    template = loader.get_template('DriftwoodMentawai.html')
    return HttpResponse(template.render())

def LovelyBeachVilla(request):
    template = loader.get_template('LovelyBeachVilla.html')
    return HttpResponse(template.render())

def PiugusResort(request):
    template = loader.get_template('PiugusResort.html')
    return HttpResponse(template.render())

def ThePalms(request):
    template = loader.get_template('ThePalms.html')
    return HttpResponse(template.render())

def AframeCabinarchitectshouse(request):
    template = loader.get_template('AframeCabinarchitectshouse.html')
    return HttpResponse(template.render())

def GreenGoldCoastalAgroResort(request):
    template = loader.get_template('GreenGoldCoastalAgroResort.html')
    return HttpResponse(template.render())

def JungleStudioBungalow(request):
    template = loader.get_template('JungleStudioBungalow.html')
    return HttpResponse(template.render())

def RiversideNest(request):
    template = loader.get_template('RiversideNest.html')
    return HttpResponse(template.render())

def RusticTwoRoomRestoredHouse(request):
    template = loader.get_template('RusticTwoRoomRestoredHouse.html')
    return HttpResponse(template.render())

def southernhouse(request):
    template = loader.get_template('southernhouse.html')
    return HttpResponse(template.render())

def FolktalesaBoutiqueHomestayArtistRetreat(request):
    template = loader.get_template('FolktalesaBoutiqueHomestayArtistRetreat.html')
    return HttpResponse(template.render())

def MachermoLodgeBakery(request):
    template = loader.get_template('MachermoLodgeBakery.html')
    return HttpResponse(template.render())

def PristineCamps(request):
    template = loader.get_template('PristineCamps.html')
    return HttpResponse(template.render())

def ZostelChitkul(request):
    template = loader.get_template('ZostelChitkul.html')
    return HttpResponse(template.render())

def ZostelShangarh(request):
    template = loader.get_template('ZostelShangarh.html')
    return HttpResponse(template.render())

def ZostelSissu(request):
    template = loader.get_template('ZostelSissu.html')
    return HttpResponse(template.render())



