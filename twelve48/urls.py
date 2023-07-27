"""
URL configuration for twelve48 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('Helpcentre',views.Helpcentre,name='Helpcentre'),
    path('cancellation',views.cancellation,name='cancellation'),
    path('termsandconditions',views.termsandconditions,name='termsandconditions'),
    path('Howwework',views.Howwework,name='Howwework'),
    path('reservesuccess',views.reservesuccess,name='reservesuccess'),

    
    path('reserves/<str:pname>',views.reserves,name='reserves'),
    path("addData",views.addData,name="addData"),
    
    path('reserveforms',views.reserveforms,name='reserveforms'),
    path("addDatas",views.addDatas,name="addDatas"),


    path('allarctic',views.allarctic,name='allarctic'),
    path('alldesign',views.alldesign,name='alldesign'),
    path('allfarms',views.allfarms,name='allfarms'),
    path('allisland',views.allisland,name='allisland'),
    path('alltinyhome',views.alltinyhome,name='alltinyhome'),
    path('alltopofworld',views.alltopofworld,name='alltopofworld'),

    path('FolvikaEye',views.FolvikaEye,name='FolvikaEye'),

    path('Hillagammi',views.Hillagammi,name='Hillagammi'),
    path('TheArcticHideaway',views.TheArcticHideaway,name='TheArcticHideaway'),
    path('StraumenSeaViewMagicArcticGetaway',views.StraumenSeaViewMagicArcticGetaway,name='StraumenSeaViewMagicArcticGetaway'),
    path('OlleroEcoLodge',views.OlleroEcoLodge,name='OlleroEcoLodge'),
    path('HuskyDreamsTipi',views.HuskyDreamsTipi,name='HuskyDreamsTipi'),
    path('Aurahouse',views.Aurahouse,name='Aurahouse'),
    path('IKSHAA',views.IKSHAA,name='IKSHAA'),
    path('JimmysVilla4BHKwPoolAssagaonAnjuna',views.JimmysVilla4BHKwPoolAssagaonAnjuna,name='JimmysVilla4BHKwPoolAssagaonAnjuna'),
    path('LaZamoravilla',views.LaZamoravilla,name='LaZamoravilla'),
    path('MarbleSunvilla',views.MarbleSunvilla,name='MarbleSunvilla'),
    path('VillaPadma',views.VillaPadma,name='VillaPadma'),
    path('FlowerValleyPlantation',views.FlowerValleyPlantation,name='FlowerValleyPlantation'),
    path('FootprintWildernessExperience',views.FootprintWildernessExperience,name='FootprintWildernessExperience'),
    path('LalaLandFarmResort',views.LalaLandFarmResort,name='LalaLandFarmResort'),
    path('SerenityHomestay',views.SerenityHomestay,name='SerenityHomestay'),
    path('VanandhaaraCoorg',views.VanandhaaraCoorg,name='VanandhaaraCoorg'),
    path('WhisperingWatersArtistCottage',views.WhisperingWatersArtistCottage,name='WhisperingWatersArtistCottage'),
    path('BeautifulOceanfrontCabana',views.BeautifulOceanfrontCabana,name='BeautifulOceanfrontCabana'),
    path('cubacali',views.cubacali,name='cubacali'),
    path('DriftwoodMentawai',views.DriftwoodMentawai,name='DriftwoodMentawai'),
    path('LovelyBeachVilla',views.LovelyBeachVilla,name='LovelyBeachVilla'),
    path('PiugusResort',views.PiugusResort,name='PiugusResort'),
    path('ThePalms',views.ThePalms,name='ThePalms'),
    path('AframeCabinarchitectshouse',views.AframeCabinarchitectshouse,name='AframeCabinarchitectshouse'),
    path('GreenGoldCoastalAgroResort',views.GreenGoldCoastalAgroResort,name='GreenGoldCoastalAgroResort'),
    path('JungleStudioBungalow',views.JungleStudioBungalow,name='JungleStudioBungalow'),
    path('RiversideNest',views.RiversideNest,name='RiversideNest'),
    path('RusticTwoRoomRestoredHouse',views.RusticTwoRoomRestoredHouse,name='RusticTwoRoomRestoredHouse'),
    path('southernhouse',views.southernhouse,name='southernhouse'),
    path('FolktalesaBoutiqueHomestayArtistRetreat',views.FolktalesaBoutiqueHomestayArtistRetreat,name='FolktalesaBoutiqueHomestayArtistRetreat'),
    path('MachermoLodgeBakery',views.MachermoLodgeBakery,name='MachermoLodgeBakery'),
    path('PristineCamps',views.PristineCamps,name='PristineCamps'),
    path('ZostelChitkul',views.ZostelChitkul,name='ZostelChitkul'),
    path('ZostelShangarh',views.ZostelShangarh,name='ZostelShangarh'),
    path('ZostelSissu',views.ZostelSissu,name='ZostelSissu'),

    
]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)