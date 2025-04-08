IMAGING INFRARED SEEKER DESIGN

A THESIS SUBMITTED TO
THE GRADUATE SCHOOL OF NATURAL AND APPLIED SCIENCES
OF
MIDDLE EAST TECHNICHAL UNIVERSITY

BY

AHMET ?NAL

IN PARTIAL FULFILLMENT OF THE REQUIREMENT
FOR
THE DEGREE OF MASTER OF SCIENCE
IN
PHYSICS

JUNE, 2014

Approval of the thesis:

IMAGING INFRARED SEEKER DESIGN

submitted  by  AHMET  ?NAL  in  partial  fulfillment  of  the  requirements  for  the

degree  of  Master  of  Science  in  Physics  Department,  Middle  East  Technical

University by,

Prof. Dr. Canan ?zgen

Dean, Graduate School of Natural and Applied Sciences

____________________

Prof. Dr. Mehmet T. Zeyrek

Head of Department, Department of Physics

____________________

Assoc. Dr. Serhat ?ak?r

Supervisor, Department of Physics, METU

____________________

Examining Committee Members

 Assoc. Prof. Dr. ?smail Rafatov

Department of Physics, METU

Assoc. Prof.  Dr. Serhat ?ak?r

Department of Physics, METU

Assist. Prof. Dr Kemal Efe Eseller

____________________

____________________

Department  of  Electrical  &  Electronic  Engineering,

____________________

At?l?m University

Assoc. Prof. Dr. Burak Yedierler

Department of Physics, METU

Assist. Prof. Dr. Alpan Bek

Department of Physics, METU

____________________

____________________

Date :

30.06.2014

I  hereby  declare  that  all  information  in  this  document  has  been  obtained  and

presented in accordance with academic rules and ethical conduct. I also declare

that, as  required by these rules and conduct, I have fully cited and referenced

all material and results that are not original to this work.

Name, Last Name:  Ahmet ?NAL

Signature :

iv

ABSTRACT

IMAGING INFRARED SEEKER DESIGN

?nal, Ahmet

M. Sc., Department of Physics

Supervisor: Assoc. Prof. Dr. Serhat ?ak?r

June 2014, 78 pages

The subject of this study is the design of an imaging infrared seeker for aerial targets.

Firstly  the  radiant  power  of  the  target  was  discussed  and  optical  design  of  seeker

lenses  were  done  with  ZEMAX  Optical  Design  Software  considering  the  MTF

(Modulation  Transfer  Function)  values,  optical  path  differences,  distortions  and

detection range calculations.  After that, detection range calculations and simulation

results of the optical system were presented.

Before  lock  on  range  calculations,  spectral  band  of  the  system  was  analyzed  and

chosen  for  aerial  targets.  After  that,  lock  on  range  was  calculated  considering

detector  noise,  background  noise  and  target  radiation.  Afterward  the  optical

parameters  of  the  seeker  were  determined.  Focal  length  and  F#  (F-number)  of  the

seeker was calculated as it was receiving the aerial target and background radiation at

5 km distance. Design was done using ZEMAX optical design program.  Moreover,

the  lens  materials  were  Silicon,  Germanium  and  Cadmium  Selenide  and  Sapphire

were dome material. Finally, optical performance parameters have been analyzed.

Finally, test plate fitting is applied to the optical system. Manufacturing parameters

were presented and discussed.

v

Keywords:  Infrared  Imaging,  IIR,  Optical  Design,  ZEMAX,  MWIR,  Infrared

Seeker.

vi

?Z

KIZIL?TES? ARAYICI BA?LIK TASARIMI

?nal, Ahmet

Y?ksek Lisans, Fizik B?l?m?

Tez Y?neticisi : Do?. Dr. Serhat ?ak?r

Haziran 2014, 78 sayfa

Bu ?al??mada hava hedefleri i?in k?z?l?tesi aray?c? ba?l?k tasar?m? ama?lanm??t?r. ?lk

olarak hedefin k?z?l?tesi ???n?m g?c? tart???lm??t?r ve daha sonra MTF de?erleri, optik

yol  farklar?,  distorsiyon  ve  hedefi  alg?lama  mesafesi  dikkate  al?narak  ZEMAX

program? ile optik sistem tasar?m? yap?lm??t?r. Daha sonra, hedefi alg?lama hesaplar?

ve optik tasar?m?n sonu?lar? sunulmu?tur.

Hedefe  kilitlenme  mesafesi  hesaplamalar?ndan  ?nce  hedefin  spektral  bant  aral???

analiz  edilmi?  ve  hedef  se?ilmi?tir.  Daha  sonra,  detekt?r  g?r?lt?s?,  arka  plan

g?r?lt?s? ve hedef ???mas? dikkate al?narak hedefe kilitlenme mesafesi hesaplanm??,

aray?c? ba?l???n optik parametreleri belirlenmi?tir. Aray?c? ba?l???n odak uzunlu?u ve

F#  (F  numaras?),  hedef  ve  arka  plan  ???mas?n?  5  km  mesafen  al?yormu?  gibi

hesaplanm??t?r.  Lens  malzemeleri  silikon,  germanyum  ve  kadmiyum  selenit,  dom

malzemesi  olarak  da  safir  se?ilmi?tir.  Son  olarak,  optik  performans  parametreleri

analiz edilmi?tir.

Sonu? olarak test plakalar? analizi optik sisteme uygulanm??t?r. ?retim parametreleri

sunulmu? ve tart???lm??t?r.

vii

Anahtar Kelimeler: K?z?l?tesi G?r?nt?leyici, IIR, Optik Tasar?m, ZEMAX, MWIR,

K?z?l?tesi Aray?c? Ba?l?k.

viii

To My Parents

ix

ACKNOWLEDGEMENTS

First of all, I would like to thank my supervisor Assoc. Prof. Dr. Serhat ?AKIR for

his kind guidance, cooperation, encouragement and advice throughout the study.

I would like to thank to Prof. Dr. Mehmet T. ZEYREK and Assoc. Prof. Dr. Hakan

ALTAN for their support for admission to Department of Physics.

I sincerely thank to RST Uzaktan Alg?lama ve G?v. Tekn. Bil. Elk. Dan. M?h. Mim.

Tic.  A.?.  and  the  managers  for  giving  me  the  chance  to  complete  my  Master  of

Science degree.

Finally,  I  would  like  to  thank  my  family  for  their  continuous  support  and

encouragement through all my life.

x

TABLE OF CONTENTS

ABSTRACT ................................................................................................................. v

?Z .............................................................................................................................. vii

ACKNOWLEDGEMENTS ......................................................................................... x

TABLE OF CONTENTS ............................................................................................ xi

LIST OF TABLES .................................................................................................... xiii

LIST OF FIGURES .................................................................................................. xiv

LIST OF ABBREVIATIONS .................................................................................. xvii

CHAPTERS

1. INTRODUCTION ........................................................................................ 1

2. BACKGROUND INFORMATION ............................................................. 3

2.1 The Electromagnetic Spectrum ...................................................... 3

2.2 The Atmospheric Transmittance .................................................... 4

2.3 Radiometry & Thermal Radiation .................................................. 5

2.4 Signature Estimation of an Aircraft .............................................. 11

2.5 Optical Design Parameters ........................................................... 12

2.5.3 Diffraction, Aberrations and Image Quality .................. 14

2.6 Detector Parameters ...................................................................... 26

3. DEVELOPMENT OF HEAT SEEKERS .................................................. 29

3.1 Infrared Seekers ............................................................................ 31

3.1.1 First Generation Infrared Seekers .................................. 31

3.1.2 Second Generation Infrared Seekers ............................. 33

3.1.3 Third Generation Infrared Seekers ................................ 34

3.2 Imaging Infrared Seekers ............................................................. 35

3.2.1 Scanning Infrared Seekers ............................................. 36

xi

3.2.2 Staring Infrared Seekers ................................................. 37

3.2.3 Dual Band Staring Infrared Seekers .............................. 38

4. SYSTEM DESIGN ..................................................................................... 39

4.1 Detection Range Calculations....................................................... 39

4.2 Optical Design of Seeker Objective ............................................. 45

4.3 Optical System Performance Parameters...................................... 60

5. DISCUSSION AND CONCLUSION ........................................................ 67

REFERENCES ........................................................................................................... 71

APPENDICES

A. SOFTWARE CODES OF ÅgINFRARED RANGE AND NETD

CALCULATORÅh ........................................................................................... 75

xii

LIST OF TABLES

TABLES

Table 1.1 Emissivity values at 300 K [3] ..................................................................... 9

Table 4.1 Detector parameters [17] ............................................................................ 41

Table 4.2 Optical parameters ..................................................................................... 46

Table 4.3 Lens parameters for case 1 ......................................................................... 47

Table 4.4 Lens parameters for case 2 ......................................................................... 49

Table 4.5 Lens parameters for case 3 ......................................................................... 51

Table 4.6 Lens parameters for case 4 ......................................................................... 53

Table 4.7 Lens parameters for case 5 ......................................................................... 55

Table 4.8 Lens parameters for case 6 ......................................................................... 57

Table 4.9 Lens parameters for case 7 ......................................................................... 59

Table 5.1 Lens parameters after test plate fitting ....................................................... 68

xiii

LIST OF FIGURES

FIGURES

Figure 2.1 Electromagnetic spectrum and infrared sub regions [2] ............................. 4

Figure 2.2 Atmospheric transmittance in infrared region [6] ....................................... 5

Figure 2.3 Schematic representation of KirchhoffÅfs law ............................................. 6

Figure 2.4 Spectral radiance exitance versus wavelength graph .................................. 8

Figure 2.5 Different types of emissivity ....................................................................... 8

Figure 2.6 Solid angle model ..................................................................................... 10

Figure 2.7 An aircraft model [4] ................................................................................ 11

Figure 2.8 Lens parameters ........................................................................................ 12

Figure 2.9 Optical system specifications .................................................................... 14

Figure 2.10 Focus points of a) theoretical and b) real lenses ..................................... 15

Figure 2.11 Spherical aberration ................................................................................ 16

Figure 2.12 Reducing spherical aberration ................................................................ 16

Figure 2.13 Optical aberration of a) coma, b) spot size of different fields. ............... 17

Figure 2.14 Different aperture stop positions are shown in  a) coma with stop in front

of lens, b) reduced coma with stop after lens ............................................................. 18

Figure 2.15 Astigmatism [15] .................................................................................... 20

Figure 2.16 Field curvature ........................................................................................ 20

Figure 2.17 Distortion ................................................................................................ 21

Figure 2.18 Chromatic aberrations a) Longitudinal chromatic aberration b) Lateral

chromatic aberration ................................................................................................... 22

Figure 2.19 Optical path difference (OPD) ................................................................ 23

Figure 2.20 Image of a point source with different optical path difference due to

coma ........................................................................................................................... 24

Figure 2.21 Meaning of the modulation transfer function ......................................... 25

Figure 2.22 Typical MTF curves ................................................................................ 26

Figure 3.1 Schematic representation of a heat seeker and target (FOV; Field of view)

 .................................................................................................................................... 30

xiv

Figure 3.2 Heat seekers block diagram ...................................................................... 30

Figure 3.3 Reticle structure and the detector output pulse [11] ................................. 32

Figure 3.4 Optical structure of the 1. generation infrared seekers [12] ..................... 33

Figure 3.5 Time domain analysis a) no target, b) target, c) target in different angular

position than case b). .................................................................................................. 33

Figure 3.6 Structure and Its output of the con-scan reticle seeker [12] ..................... 34

Figure 3.7 Optical structure of the rosette scanning infrared seeker (f1 and f2 rotating

frequencies of prisms) ................................................................................................ 35

Figure 3.8 Working geometry of the rosette-scan seekers [14] ................................. 35

Figure 3.9 Schematic representation of scanning infrared seeker optic ..................... 36

Figure 3.10 Optical representation of refractive imaging infrared seeker ................. 37

Figure 3.11 Optical representation of reflective imaging infrared seeker ................. 38

Figure 4.1 Spectral radiant exitance graph for a) 750 K,600 K and 500 K objects, b)

background 300 K object ........................................................................................... 40

Figure 4.2 Cold shield and F/# ................................................................................... 42

Figure 4.3 Infrared range and NETD calculator software interface ........................... 43

Figure 4.4 Background dimension calculation........................................................... 44

Figure 4.5 Solid angle calculations. ........................................................................... 45

Figure 4.6 FOV calculation for optical system .......................................................... 46

Figure 4.7 Zemax simulations for case 1; a) optical system, b) spot sizes for different

fields. .......................................................................................................................... 48

Figure 4.8 Zemax simulations for case 2; a) optical system, b) spot sizes for different

fields. .......................................................................................................................... 50

Figure 4.9 Zemax simulations for case 3; a) optical system, b) spot sizes for different

fields. .......................................................................................................................... 52

Figure 4.10 Zemax simulations for case 4; a) optical system, b) spot sizes for

different fields. ........................................................................................................... 54

Figure 4.11 Zemax simulations for case 5; a) optical system, b) spot sizes for

different fields. ........................................................................................................... 56

Figure 4.12 Zemax simulations for case 6 ; a) optical system, b) spot sizes for

different fields. ........................................................................................................... 58

xv

Figure 4.13 Zemax simulations for case 7; a) optical system, b) spot sizes for

different fields. ........................................................................................................... 60

Figure 4.14 OPD of the optical system a) 0Åã field, b) 3Åã field and c) 3.7Åã field ........ 62

Figure 4.15 Distortion of the optical system .............................................................. 64

Figure 4.16 MTF of the optical system ...................................................................... 66

xvi

LIST OF ABBREVIATIONS

AM

AP

ATA

ATR

CA

CT

EFL

ET

FOR

FOV

FP

: Amplitude Modulation

: Amplitude Phase Modulation

: Automatic Target Acquisition

: Automatic Target Recognition

: Clear Aperture

: Center Thickness

: Effective Focal Length

: Edge Thickness

: Fields of Regard

: Field of View

: Frequency Phase Modulation

IFOV

: Instantaneous Field of View

IIR

InSb

IR

: Imaging Infrared

: Indium Antimonite

: Infrared

LWIR

: Long Wave Infrared

MTF

: Modular Transfer Function

MWIR

: Mid Wave Infrared

NIR

OPD

SNR

: Near Infrared

: Optical Path Difference

: Signal to Noise Ratio

SWIR

: Short Wave Infrared

xvii

    CHAPTER 1

1. INTRODUCTION

For  surface  to  air  missiles  and  air  to  air  missiles,  one  of  the  examples  of  homing

guidance is imaging infrared homing and it is used to detect the angular position of

the target with respect to missile axis.

The objective of this study is to design an imaging infrared seeker. SeekerÅfs spectral

region is usually determined by the target radiation spectrum. In our case the target is

an  aircraft  and  it  radiates  in  MWIR  and  LWIR  regions  of  the  electromagnetic

spectrum due to the temperature of the object.

Detection  range  of  a  seeker  is  related  with  atmospheric  transmission,  background

radiation,  optical  transmission  of  the  optical  components,  F#  (F-number)  of  the

optical  system  and  the  noise  of  the  detector  [3].  Most  popular  imaging  sensor

materials  in  the  MWIR  range  are  HgCdTe  (Mercury  Cadminium  Telluride),  PbS

(Lead  Sulfide) and  InSb  (Indium Antimonide).  An  InSb detector array  was  used in

this work. Other sensors may also be used instead of InSb detector.

Atmospheric transmission in infrared band is sensitive to the atmospheric conditions

such  as  snow,  rain,  haze,  smoke,  dust  and  it  depends  on  wavelength  [3].  So  the

performance of the optical system or seeker depends on the atmospheric transmission

conditions. In the world, many companies or scientific research labs use MODTRAN

Software  (Moderate  Resolution  Transmittance  Code)  to  calculate  the  atmospheric

transmission

in  related  wavelength  region.  In

this

thesis,

the  atmospheric

transmission will be taken from the literature.

1

The seeker was designed to detect a target at 5 km distance. MissileÅfs diameter was

assumed to be 140 mm and seekerÅfs optics was assumed to be rotated as Å}90Åã. So

the  space  requirement  for  the  seeker  optics  was  determined  as  70  mm.  Refractive

optical components were used in the optical system. Rayleigh criteria and pixel pitch

of the detector were taken into account for optical performance.

ZEMAX  optical  design  program  was  used  to  reach  the  best  performance.  Lens

parameters such as lens material, radius, thickness and distance between lenses were

optimized  for  different  cases.  Generally,  Hammer  optimization  was  used  in  this

work. Hammer optimization provides glass substitution. So that, lens conjugates that

must  be  used  in  an  optical  design  was  determined  by  this  method.  Also  the

performance criterions like spot diagrams, MTF, distortion were discussed.

In the following chapters, the details of the study are presented.

In Chapter 2 basic definitions of infrared bands are given. The radiometric quantities

are  discussed  for  a  typical  aircraft.  Basic  definitions  and  brief  information  about

optical system design are also given and system parameters are defined.

In  Chapter  3  the  heat  seekers  and  heat  seeker  types  are  explained  in  working

mechanisms. Future of heat seekers is also discussed.

In Chapter 4 the target radiation spectral band is determined by its temperature. After

that lock on range calculation equations are carried out to find the detection range of

a  seeker  at  5  km.  The  optical  system  requirements  are  determined.  Finally  optical

system design was done using ZEMAX optical design software. Results were plotted

and discussed.

In  Chapter  5  the  study  is  completed  with  discussion  of  the  seeker  and

manufacturability of the system.

2

CHAPTER 2

2. BACKGROUND INFORMATION

2.1 The Electromagnetic Spectrum

The electromagnetic spectrum is distribution of all possible electromagnetic radiation

according

to  energy,  frequency  or

it

is

the  characteristic  distribution  of

electromagnetic radiation emitted or absorbed by a particular object [3].

The  electromagnetic  spectrum  is  the  electromagnetic  waves  from  low  frequencies

(radio  communication)  to  high  frequencies  (gamma  radiation).  Upper  limit  of

electromagnetic  spectrum  for  long  wavelength  is  the  universe  and  lower  limit  for

short wavelength is in the vicinity of the Planck length [3, 7].

The electromagnetic spectrum is shown in Fig. 2.1 with infrared part between radio

and visible waves. The infrared spectrum is divided into 5 sub regions, although this

definition is arbitrary and it can change from one author to another [2].

The infrared region shown in Fig. 2.1 is based on a combination of the atmospheric

transmittance  and  wavelength.  In  infrared  region  some  subregions  have  better

transmittance  while  other  regions  have  no  transmittance.  The  subregions  or

wavelength  intervals  that  have  better  transmittance  are  called  Ågatmospheric

windowsÅh. Infrared sensors or detectors are especially designed for these wavelength

intervals.  In  this  way,  the  near  infrared  (NIR)  band  is  mostly  used  in  fiber  optic

telecommunication  systems,  whilst  the  short  wave  infrared  (SWIR)  band  allows  to

3

work on long-distance telecommunications (remote sensing) using a combination of

detector  materials.  The  medium  wavelength  infrared  (MWIR)  and  the  long

wavelength  infrared  (LWIR)  bands  find  applications  in  infrared  thermography  for

military  or  civil  applications,  e.g.  target  signature  identification,  surveillance,  etc.

The  very  long  wavelength  Infrared  (VLWIR)  band  is  used  in  spectroscopy  and

astronomy [2].

Figure 2.1 Electromagnetic spectrum and infrared sub regions [2]

2.2 The Atmospheric Transmittance

In Fig. 2.2, four of five main atmospheric windows of infrared: NIR, 0.74 to 1 ?m,

SWIR, 1 to 3 ?m, MWIR, 3 to 5 ?m and LWIR, 8 to 14 ?m are shown. Most of the

infrared systems use this band to develop infrared systems [2,3].

4

The  atmosphere  is  a  gaseous  combination  of  CO2,  H2O,  N2,  O2  and  O3  molecules.

Because of the molecular vibration of these, absorption attenuates the transmission of

the infrared radiation. Attenuation also comes from the scattering by particles in the

atmosphere. Fig. 2.2 shows the infrared bands and molecules that causes absorption.

NIR  and  LWIR  bands  are  affected  by  water  vapor  and  MWIR  band  is  affected  by

CO2 and O3 [2].

Figure 2.2 Atmospheric transmittance in infrared region [6]

Atmospheric transmittance is given by [9];

                                              (2.1)

where É– is called extinction coefficient determined by absorption and scattering and

it is a function of wavelength. R is the distance (or range) to be calculated [20]. The

equation  shows  the  atmospheric  transmittance  of  the  weather  and  it  is  function  of

wavelength and range.

2.3 Radiometry & Thermal Radiation

Thermal radiation of very hot objects can be seen by human eye because the thermal

emission of the object is in the visible region of the electromagnetic spectrum. As an

5

ReT)()(?????

example,  the  SunÅfs  temperature  is  approximately  6000  K  and  it  can  be  seen  by

human eye. For objects at room temperature, the thermal radiation is in the infrared

region. So, it can be seen by special detectors [7].

Radiometry is a quantitative analysis of flux from thermal radiation transfer between

optical system and an emitter object. The radiated emission from an object transmits

through the atmosphere and it is collected by optics. Radiometry is used to calculate

the optical power that is needed to generate electrical signal on detector [3].

Total  incident  radiation  that  interacts  with  an  object  is  equal  to  sum  of  absorbed,

reflected  and  transmitted  part  of  incident  radiation  or  sum  of  Transmittance  (T;

transmitted  energy  over  incident  energy),  Absorbance  (Éœ;  absorbed  energy  per

incident energy) and Reflectance (Éø; reflected energy per incident energy) [3]. This is

called KirchhoffÅfs Law.  It can be formulized as

                                                   (2.2)

It  is  also  called  thermal  equilibrium  and  KirchhoffÅfs  law  is  wavelength  dependent

absorption, emission at thermal equilibrium.

Figure 2.3 Schematic representation of KirchhoffÅfs law

6

1???T??Incident RadiationReflected RadiationTransmitted RadiationEmitted RadiationOBJECTAbsorbed Radiation

Emissivity  is  a  dimensionless  quantity  and  it  shows  how  much  of  the  radiation  is

emitted from the object. It is equal to absorbed radiation of the object. If an object is

good absorber, it is already a good emitter (

(emissivity), blackbody) [3].

When an object absorbs all incoming radiation strikes on it in all wavelengths, it is

called ÅgblackbodyÅh. It does not transmit or reflect any part of the incident radiation.

For  blackbody

,

  and

.  Blackbody  objects  emit  maximum

radiation of the objects at any temperature [3].

ÅgRadiant ExitanceÅh is the radiant power from a surface per area and it is a function of

temperature and wavelength. ÅgSpectral Radiant ExitanceÅh is the radiant power from

a  surface  per  area,  per  wavelength.  The  relation  between  spectral  radiant  exitance

and radiant exitance is [3]

                                                   (2.3)

MÉ…  is  the  symbol  of  the  spectral  radiant  exitance  and  the  unit  is  watt  per  area  per

wavelength  and  the  M  is  the  spectral  radiant  exitance  and  the  unit  is  watt  per  unit

area.

 and

 are the wavelength interval. Blackbody radiation can be specified by

PlanckÅfs equation is [3]

                                         (2.4)

where  h  is  the  PlankÅfs  constant,  k  is  the  BoltzmanÅfs  constant,  T  is  the  temperature

and  c  is  the  speed  of  light.  Fig.  2.4  shows  spectral  radiance  exitance  versus

wavelength corresponding to specific temperatures.

7

???1????0??0?T????dMM??211?2?1)exp(1252,??kThchcMBB????

Figure 2.4 Spectral radiance exitance versus wavelength graph

When the emissivity É√<1, it is called grey body and some materials have emissivity

that is a function of wavelength.

Figure 2.5 Different types of emissivity

Emissivity can be constant  or a function of wavelength.  Emissivity values  of some

materials are shown in the Table 1.

8

Table 1.1 Emissivity values at 300 K [3]

Material

Emissivity

Aluminum

Highly Polished Copper

Stainless Steel

Brick

Carbon

Glass

Sand

Human Skin

Distilled Water

Snow

Wood

0.05

0.02

0.16

0.93

0.95

0.94

0.90

0.98

0.96

0.90

0.9

By definition of blackbody, emissivity can be defined the ratio of spectral exitance of

the object to the spectral exitance to the reference blackbody [3].

                                           (2.5)

If the object  is  blackbody, É√ is  equal  to  1.  If not,  then spectral  radiance exitance is

defined as

                                       (2.6)

Emissivity can be a constant or a function of wavelength for real objects.

ÅgSolid  angleÅh  Åg?Åh  is  an  angle  in  3  dimensional  space  and  it  shows  how  large  the

object is seen from the observer position.  It is dimensionless and measured in square
9

??????00,),(),()(??????????dTMdTMMMBBObject??21),()(???????dTMMObject

radians  or  steradians  (sr)  [3].  Fig.  2.6  shows  the  geometric  representation  of  solid

angle and it can be described as

                                                          (2.7)

where ? is the area of the surface on sphere and r is the distance from the source.

Figure 2.6 Solid angle model

Radiance  exitance  per  unit  solid  angle  is  defined  as  ÅgRadianceÅh  and  can  be

formulized as

                                                 (2.8)

where  L  is  the  radiance  and  unit  is  Watt  per  unit  area  per  unit  steradian  and

spectral radiance exitance for nonblackbody object but same equation can be written

10

2ra??r? Area = ? ???????2/020sin??????LdLdLdM?????dML??211?M

for  blackbody.  In  this  situation

will  be

  and  radiance  will  be  blackbody

radiance [3].

2.4 Signature Estimation of an Aircraft

The  signature  of  the  target  is  variable  from  target  to  another  target  because  every

companyÅfs  aerial  vehicle  has  specific  exitance  from  exhaust  and  remote  sensing

designers have to make an estimation to find the target signature model [9]. Fig. 2.7

shows  an  aircraft  model  for  estimation  of  the  target  radiation.  In  Fig.  2.7  red  parts

shows  hot  parts  of  aircraft.  Nose,  engine  inlets  and  leading  edges  cause  from

aerodynamic heats and exhaust plume comes from engine temperature.

Figure 2.7 An aircraft model [4]

The  target  can  be  divided  into  n  area  elements  where  the  radiance  is  uniform  over

each element. The total radiance that is emitted by the aircraft

                                           (2.9)

where É√i, is emissivity of each element, MÉ…i is the spectral radiance exitance of each

element and Ai is the area of the each element. Each element that shown in the Fig.

2.7  are  in  different  temperatures  and  maximum  radiation  is  emitted  from  engine

11

?MBBM,????niiTOTALdMLi??????211

nozzles.  There  are  many  radiation  sources  such  as  plume,  hot  parts,  skin,  reflected

sky  shine,  reflected  earthshine,  reflected  clouds.  These  sources  make  an  exact

determination  of  the  signature  for  an  arbitrary  aircraft  virtually  impossible.  So,  to

make calculation simpler some assumptions has to done. The assumptions are

?  The  aerial  platform  is  assumed  to  radiate  as  a  gray  body.  In  addition,  the

emissivity for all elements of the aircraft is assumed to be unity.

?  The temperature is assumed to be uniform over sources.

?  Aerodynamic heating effects are neglected.

?  Maximum radiating element is considered as a main radiation source [9].

As a result the 2.9 can be simplified to

                                               (2.10)

where É…1 and É…2 are the wavelength limits of the infrared band.

2.5 Optical Design Parameters

Single lens and parameters are shown in Fig. 2.8.

Figure 2.8 Lens parameters

12

??211??????dMLTOTALR1R2Optical AxisPÅfPETCTEFLBFLFFLEFL

  is  called  front  principle  point  of  the  lens  and

  is  called  rear  principle  point.

Plane that intersects  principle point and optical  axis  is called principle plane of the

lens. Plane that intersects

 is called front principle plane and intersects

 is called

rear principle plane.

EFL is effective focal length of the lens and it is distance from rear principle plane to

focal point of the lens. CT is center thickness and the ET is the edge thickness of the

lens. BFL is back focal length and it is distance between rear surface of the lens on

the optical axis and focal point.

is radius of the front surface and

 is radius of

the rear surface. Effective focal length of a thin lens is given as [22]

                                       (2.11)

where

 and

are radius of first and second surface. For thick lens, effective focal

length is [22]

                           (2.12)

where n is the refractive index of lens material and CT is center thickness of the lens.

F# or F-number is defined as focal length over clear aperture (it is called Ågentrance

pupil diameterÅh). F# is given as

                                                  (2.13)

where EFL is the effective focal length and CA is the clear aperture. FOV (Field of

view) is the angle with the optical system or lens accepts light [15].

13

P'PP'P1R2R???????????2111)1(1RRnEFL1R2R?????????????2121)1(11)1(1RnRCTnRRnEFLCAEFLF?#

Figure 2.9 Optical system specifications

2.5.3 Diffraction, Aberrations and Image Quality

Aberrations  are  failure  of  the  optical  systems.  For  real  lenses  image  quality  is

degraded by aberrations. Ideal and real focuses are shown in Fig. 2.10. ÅgAiry discÅh is

called  as  an  ideal  spot  size  of  an  ideal  lens  and  its  diameter  is  given  as  2.44É…/CA

where É… is wavelength.

14

Image PlaneEFLFOV

a)

b)

Figure 2.10 Focus points of a) theoretical and b) real lenses

For optical systems or single lenses, aberrations are failures of the optical system to

produce an ideal focus in image plane. There are 6 known optical aberrations [15].

One of the aberrations is called Ågspherical aberrationÅh. As shown in Fig. 2.11, when

the ray height above the optical axis, the rays in image space cross the axis or focus

closer  and  closer  to  the  lens.  This  change  of  focus  position  in  focal  point  is  called

spherical aberration.

15

Paraxial LensImage PlaneAiry DiscDouble Convex LensImage Plane

Figure 2.11 Spherical aberration

As shown in Fig. 2.12  spherical  aberrations can  be reduced by splitting the lens or

lens bending [15].

Figure 2.12 Reducing spherical aberration

For minimum spherical aberration for single lens

is given as [22]

                                       (2.14)

16

Double Convex LensImage PlaneParaxial FocusDifferent Lens BendingsLens Splitting1REFLnnnnR)12()1)(2(21????

for

                                      (2.15)

Another optical aberration is called ÅgcomaÅh. If the rays enter to the lens with angle,

this causes coma aberration. As shown in Fig. 2.13 every ray is focused by the lens to

a certain height from the optical axis [15].

a)

b)

Figure 2.13 Optical aberration of a) coma, b) spot size of different fields.

17

2REFLnnnnR4)12()1)(2(22?????Meniscus LensFocus for 10 Åã FieldFocus for 0 Åã FieldImage Plane

As shown in Fig. 2.14 Coma can be reduced changing the aperture stop of the optical

system.

a)

Figure 2.14 Different aperture stop positions are shown in  a) coma with stop in front

of lens, b) reduced coma with stop after lens

18

Meniscus LensFocus for 10 Åã FieldFocus for 0 Åã FieldImage PlaneSTOP

b)

Figure 2.14 (continued)

Another  optical  aberration  is  called  ÅgastigmatismÅh.  It  causes  from  the  rays  in  the

meridional  and  sagittal  planes  are  not  focused  at  the  same  distance  from  the  lens.

Astigmatism is shown in Fig. 2.15 [15].

19

Meniscus LensFocus for 10 Åã FieldFocus for 0 Åã FieldImage PlaneSTOP

Figure 2.15 Astigmatism [15]

Another  optical  aberration  is  called  Ågfield  curvatureÅh.  As  shown  is  Fig.  2.16,  focal

plane  is  formed  as  a  curve,  not  a  plane.  Reason  for  this  aberration  is  that  the  back

focal length changes with the field of the lens [15].

Figure 2.16 Field curvature

To reduce this aberration, there are two known methods. In first method, a negative

lens is used between two positive lenses. Another method is to locate a negative lens

near to the image plane [15].

Another  optical  aberration  is  called  ÅgdistortionÅh.  This  aberration  arises  from  the

change  of  magnification  because  of  the  field  of  view  or  distortion  effects  overall

20

Meniscus LensReal Image PlaneParaxial Image Plane

shape  of  the  image.  It  causes  depart  from  true  replica  of  the  object.    For  a  good

imaging  system,  the  distortion  should  be  less  than  2%  [1,  15].  Figure  2.17  shows

different  type  of  distortions.  If  the  distortion  dimension  is  greater  than  the  detector

dimension, the distortion is called positive distortion otherwise negative distortion.

Figure 2.17 Distortion

Final  aberration  is  called  Ågchromatic  aberrationÅh.  Refractive  index  is  a  function  of

wavelength. As a result, the focal length of the lens or effective focal length of the

optical  system  will  change  with  wavelength  in  axial  direction  and  this  is  called

Åglongitudinal  chromatic  aberrationÅh.  If  the  magnification  changes  in  the  lateral

direction with wavelength, this is called Åglateral chromatic aberrationÅh [15]. These

aberrations are shown in Fig. 2.18.

21

zero distortionpositive or pincushion distortionnegative or barrel distortion

a)

b)

Figure 2.18 Chromatic aberrations a) Longitudinal chromatic aberration b)
Lateral chromatic aberration

For an imaging optical system, OPD (optical path difference) is a method to measure

the optical performance. As shown in Fig. 2.19, OPD is difference between the real

wavefront  and  a  spherical  wavefront  (ideal  wavefront  for  perfect  focus).  The  real

wavefront departs from the spherical wavefront [15].

22

Plano Convex LensFocus Point For Blue LightFocus Point For Red LightFocus Point For Green LightPlano Convex LensImage PlaneFocus Point For Green waveFocus Point For Blue wave

Figure 2.19 Optical path difference (OPD)

Lord Raleigh (real name is William Strutt, a Nobel Prize winner for discovering the

gas argon) showed that [15]

ÅgAn  optical  instrument  would  not  fall  seriously  short  of  the  performance  possible

with  an  absolutely  perfect  system  if  the  distance  between  the  longest  and  shortest

paths leading to a selected focus did not exceed one-quarter of a wavelength.Åh

As shown in Fig. 2.20, the image of a point source (which is known as a point-spread

function) for different optical path differences cause different focuses. Note that the

0.25 wave OPD is nearly indistinguishable from the perfect airy disc [15].

23

Spherical WavefrontReal WavefrontOPDOPDExit pupil diameter

0 É… Perfect Airy Disc

0.25 É…

0.5 É…

1 É…

Figure 2.20 Image of a point source with different
optical path difference due to coma

MTF is the most comprehensive of all optical system performance criteria, especially

for  image  forming  systems.  The  imagery  will  be  degraded  due  to  aberrations,

assembly  and  alignment  errors.  MTF  measures  how  the  lens  system  transfers  the

modulation (or contrast) of the object to the image plane. Definition of MTF is

Modulation=

                                           (2.15)

where

 is the maximum intensity and

 is the minimum intensity. MTF shows

how the object space is degraded in image plane after passing the optical system. Fig.

2.21 shows the object and image plane modulations.

24

minmaxminmaxIIII??maxIminI

Figure 2.21 Meaning of the modulation transfer function

MTF is a function of spatial frequency and the cutoff frequency, which is where the

MTF goes to zero, is

                                                    (2.16)

Fig. 2.22 shows a graphical representation of an object and of the resulting image at a

low spatial frequency, a midspatial frequency and at high spatial frequency regions in

spatial frequency domain [15].

25

After Optical SystemIntensityObject PlaneImage PlanemaxIminIIntensitymaxIminI)/#(1fcutoff???

Figure 2.22 Typical MTF curves

2.6 Detector Parameters

In  MWIR  infrared  band,  QWIP  (quantum  well  infrared  photodetector)  and

Photoconductive type detectors are used mostly. These are all semiconductor based

and  are  processed  in  clean  room  as  a  detector  arrays  and  every  detector  element  is

called Ågpixel pitchÅh.

NETD  (noise  equivalent  temperature  difference)  and  D*  (Specific  detectivity)

parameters  are  mostly  commonly  used  parameters  that  show  the  infrared  detector
performance. D* is given as

                                                    (2.17)

26

Perfect Optical SystemsReal Optical SystemscutoffObject SpaceImage SpceIntensityIntensityNEPfADd??*

where Ad is detector area and ?f is the noise bandwidth of the detector and NEP is the

noise equivalent power which means that it is radiant flux to generate the signal to

noise ratio is equal to 1.

Another detector parameter is NETD and it is given as

                       (2.18)

                         (2.19)

where  F#  is  the  F  number  of  optical  system,

  is  the  detector  pixel  area,

is  the

transmission of optical system, É√ is emissivity,

is the absorption coefficient of

detector,

  spectral  radiant  exitance  of  blackbody  and  NEP  is  the  noise

equivalent power. NETD is generally measured at the 25 ÅãC Blackbody and with no

optics for MWIR detectors [5,19].

27

*,2#21)(114DfdTMAFNETDBBoptp??????????????NEPdTMAFNETDBBoptp?????21,2#)(114????????pA?)(??BBM,?

28

CHAPTER 3

3. DEVELOPMENT OF HEAT SEEKERS

Infrared  homing  is  a  passive  missile  guidance  system  that  uses  infrared  emissions

from aircraft to detect and lock on to the target. Missiles which use infrared seeking

are  called  as  "heat-seekers"  and  many  aircrafts  have  been  lost  in  warfare  by  heat

seekers. Objects such as people, vehicle engines and aircraft emit heat as a radiation

source and this radiation can be detectable by special detectors [10].

Radiations emitted from target and radiations emitted from background (sky) are in

different  temperatures  (For  air  temperature  is  22  ÅãC  and  for  Helicopter  exhaust

temperature  is  about  500  ÅãC).  This  difference  can  be  discriminated  using  optical

systems  and  the  angular  position  of  the  target  can  be  determined  by  using

temperature  difference  of  the  target  from  background.  The  entire  heat  seekers  use

this  principle  with  their  specific  working  mechanisms.  Schematic  representation  of

target, background and heat seeker are shown in Fig. 3.1.

29

Figure 3.1 Schematic representation of a heat seeker and target (FOV; Field of view)

Heat-Seekers  can  be  divided  into  two  divisions  as  IR  seekers  and  IIR  (imaging

infrared)  seekers  according  to  working  mechanism  how  they  find  the  angular

position  of  target  relative  to  the  optical  axis  of  heat  seeker  using  temperature

difference between target  and background. And  also they can be divided into more

sub regions shown in the Fig. 3.2.

Figure 3.2 Heat seekers block diagram

30

3.1 Infrared Seekers

Usually, IR seekers have single detector and they use a rotating ÅgreticleÅh to detect the

angular  position  of  target.  Optical  system  is  used  to  collect  and  focus  the  infrared

radiation  from  background  and  target  onto  the  detector.  Rotating  reticle  is  used  to

modulate  (Frequency,  Amplitude)  the  infrared  radiation  on  the  detector.  Infrared

radiation  of  the  background  is  less  than  the  target  radiation  because  of  the

temperature and it is uniform in all scenes, but target radiation is more powerful and

comes to the optics on a specific angular position in scene. This difference is used to

detect the angular position of the target.

The  seekers  using  single  detector  have  three  types  of  scanning  method:  spin-scan,

con-scan  and  rosette-scan.  Infrared  seekers  can  be  divided  into  3  sub  regions

according to their scanning methods or working principles [11].

3.1.1 First Generation Infrared Seekers

First generation infrared seekers have a reticle as shown in Fig. 3.3. The reticle has 3

different parts. One part is fully transparent shown on the Fig. 3.3 as white, one part

is opaque shown on the Fig. 3.3 as black and the other part is semi transparent shown

on the Fig. 3.3 as gray. When reticle is rotated, the power falling from the target onto

the detector will change according to the rotating frequency and the reticle structure.

The output of the detector according the rotation of the reticle is shown in Fig. 3.3

[11].

31

Figure 3.3 Reticle structure and the detector output pulse [11]

These types of seekers are also called spin-scan seekers. The optical structure of the

spin-scan seeker is shown in the Fig. 3.4. There are four optical components, primary

mirror, secondary mirror, reticle and detector. Primary and Secondary mirror is used

to collect the radiation emitted from the target onto the detector and reticle is used to

modulate (amplitude modulation) the infrared radiation.  This type of modulation is

also called Amplitude-Phase modulation.

Target signal and reference signal is compared while finding the angular position of

target.  When  there  is  no  target  in  the  FOV  of  seeker  the  output  of  the  detector  is

shown in Fig. 3.5 a). When there is a target in the FOV of the seeker, the output of

the detector is shown is Fig. 3.5 b) and c). The difference in Fig. 3.5 b) and c) comes

from the different angular positions of the target.

32

Figure 3.4 Optical structure of the 1. generation infrared seekers [12]

a)

b)

c)

Figure 3.5 Time domain analysis a) no target, b) target, c) target in different
angular position than case b).

3.1.2 Second Generation Infrared Seekers

Second generation seekers are called con-scan seekers. It is developed according to

the drawbacks of the spin-scan seekers. When the target is on optical axes, in other

words,  the  angle between seeker and the target  is zero, spin  scan seeker  modulator

does not work because the infrared radiation falls onto center of the reticle. Another

drawback is semitransparent region of the reticle, the infrared radiation is lost %50.

So, it directly affects the lock on range of the missile.

33

Con-scan seekerÅfs optical structure is similar to the spin scan seekers. First difference

is spin-scan seekers have stationary reticle and the structure shown in the Fig. 3.6 is

combination of transparent and the opaque parts. Second difference is the secondary

mirror  is  tilted  and  rotated  instead  of  reticle.  Due  to  tilted  secondary  mirror,  the

detector output signal of the modulated infrared radiation is shown in Fig. 3.6. This

type modulation is also called Frequency-Phase modulation.

Figure 3.6 Structure and Its output of the con-scan reticle seeker [12]

3.1.3 Third Generation Infrared Seekers

Among the various IR seekers, the rosette scanning infrared seeker RSIS is a tracker

in which a single detector scans the total field of view FOV in a rosette pattern. The

rosette pattern is achieved by means of two counter-rotating optical elements such as

prisms, tilted mirrors, or off centered lenses [13].

The optical structure of this type of missile is shown in Fig. 3.7. In this figure two

wedges are counter-rotating. This provides the seeker rosette scanning property.

34

Figure 3.7 Optical structure of the rosette scanning infrared
seeker (f1 and f2 rotating frequencies of prisms)

Working geometry of the rosette-scan missile is shown in Fig. 3.8.

Figure 3.8 Working geometry of the rosette-scan seekers [14]

3.2 Imaging Infrared Seekers

Imaging infrared seekers are state of the art in infrared seeker technology. Because of

the  imaging  nature  of  the  system,  small  detector  area  (pixel  of  the  detector),

algorithms  such  as  ATR  (automatic  target  recognition)  and  ATA  (automatic  target

acquisition) makes seeker more resistance to the countermeasures such as flares.

Imaging  infrared  seekers  can  be  divided  into  3  sub  divisions  due  to  working

principles.  Scanning  infrared  seekers  has  scanning  component  such  as  mirrors  to

35

construct  the  image  to  the  line  element  detector  array.  Staring  seekers  have  no

scanning optical component it uses a focal plane array to construct the image of the

target.  Dual  band staring infrared seekers will be the future  concept  for the missile

seekers. There is no such a seeker but it will be developed in the future because off-

the-shelf products of dual band (MWIR and LWIR) FPAs can be found in detector

companyÅfs catalogs.

3.2.1 Scanning Infrared Seekers

Scanning infrared seekers use line detector elements and try to construct the image of

the  science  using  scanning  mechanism  with  mirrors.  Working  principles  are  same

with the IIR seekers. Only, the performance of the system depends on the scanning

time of the mirrors. One of the scanning mechanisms of the scanning infrared seekers

is  shown  in  Fig.  2.32  and  scanning  infrared  seekers  can  be  subdivided  into  several

subdivisions according to the scanning mechanisms. Dome is not shown in Fig. 3.9.

Figure 3.9 Schematic representation of scanning infrared seeker optic

Because  of  the  scanning  mechanism,  working  principle  is  complex  as  in  the  IR

seekers. As in the IR seekers need and extra area in seeker for scan mirrors.

36

Scan Axis for Azimuth Scan

3.2.2 Staring Infrared Seekers

Nowadays,  imaging  infrared  seekers  are  very  popular  in  defense  industry.  Most  of

the missile seekers are using imaging infrared technology especially for aerial targets

(MWIR) and for antitank missiles (LWIR).

IIR infrared seekers can easily counter to countermeasures such as flares. Because of

the imaging nature of the system, target can be easily detected with algorithms such

as (ATA; automatic target acquisition, ATR; automatic target recognition)

3.2.2.1 Refractive Imaging Infrared Seeker

Optical representation of refractive imaging infrared seeker configuration is shown in

Fig. 3.10. The configuration has 3 optical lenses (Positive meniscus, Biconcave and

Positive Meniscus) and a focal plane array. Number of lenses and lens materials can

be changeable according to the requirements of missiles such as FOV, focal length,

weight etc. Dome is not shown in Fig. 3.10.

Figure 3.10 Optical representation of refractive imaging infrared seeker

37

Image PlanePositive MeniscusBiconcavePositive Meniscus

3.2.2.2 Reflective Imaging Infrared Seeker

Optical configuration of reflective imaging infrared seeker is shown in Fig. 3.11. The

configuration  consists  of  mirrors  to  construct  image  of  the  science  onto  the  FPA.

Mostly,  Cassegrain  optical  configuration  is  used  in  such  systems.  In  some  optical

systems  corrector  lens  groups  can  be  used  with  Cassegrain  optical  configuration.

Dome is not shown in Fig. 3.11.

Figure 3.11 Optical representation of reflective imaging infrared
seeker

3.2.3 Dual Band Staring Infrared Seekers

This  is  the  future  concept.  Dual  band  infrared  focal  plane  arrays  or  cameras  are

newly  developed.  The  cost  is  much  because  of  the  technology  of  the  detector

elements.  In  near  future  the  ÅgDual  Band  Staring  Infrared  SeekersÅh  will  be  off-the-

shelf  products.  Optical  configuration  may  be  classified  into  two  sub  categories  but

the spectrum of the band is very broad because it starts from 3?m and ends with 12

?m. This makes the optical design very hard.

38

DomePrimary MirrorCatadioptric MirrorImage PlaneCorrector Lens

 CHAPTER 4

4. SYSTEM DESIGN

4.1 Detection Range Calculations

Detection range was taken as 5 km and target was chosen as an aircraft as shown in

Fig. 2.7. The hot part of the aircraft is its nozzle and size of the nozzle was taken as
5000 cm2. Temperature of the nozzle was considered as 750 K [9]. The seeker was

designed  for  140  mm  diameter  missile.  This  diameter  may  vary  from  missile  to

missile.

Before detection range calculations, spectral region must be determined. In Fig. 4.1

Spectral Radiant Exitance is plotted as a function of wavelength.

39

a)

b)

Figure 4.1 Spectral radiant exitance graph for a) 750 K,600 K and 500 K objects, b)
background 300 K object

MWIR region has much more thermal emission than the LWIR region. Although the

nozzle of the aircraft radiates both  in LWIR and MWIR regions, detection range is

40

LWIR RegionMWIR Region600 K500 K750 KLWIR RegionMWIR Region300 K

longer in MWIR region because the radiation power is related with the temperature

of  the  object.  As  shown  in  Fig.  4.1  a)  MWIR  regionÅfs  spectral  radiance  is  greater

than  the  LWIR  region.  As  a  result,  for  high  temperature  objects,  detection  in  long

range applications, MWIR region should be used. If the target temperature was about

300 K, LWIR region would be used.

After  spectral  region  was  determined  (by  considering  the  object  temperature),

detector parameters were specified. Parameters are shown in Table 4.1

Table 4.1 Detector parameters [17]

Detector Type

InSb 2D Array

Array Format

320 x 256

Pixel Pitch

NETD

Cold Filter

Cold Shield

30 É m

20 mK

3.6 É m ? 4.9 É m

F#=3

In Table 4.1 detector type shows the detector material. Here, InSb material is used in

detector to detect the infrared radiation. ÅgArray formatÅh shows the number of pixels.

During this work 320 pixels are used in vertical direction and 256 pixels are used in

horizontal direction. ÅgPixel pitchÅh shows the dimension of the pixel. The pixel pitch

is 20 ?m. NETD is a measure of the detector sensitivity. It shows how sensitive is the

detector.  ÅgCold  filterÅh  shows  the  spectral  region  of  the  detector  and  it  is  a  narrow

window. The spectral region is between 3.6 É m and 4.9 É m. Radiation emitted from

the aircraft was considered in this interval. ÅgCold shieldÅh is  used  to  cool  the  infrared

detector. Schematic representation of the cold shield is shown in Fig. 4.2.

41

Figure 4.2 Cold shield and F/#

As  shown  Fig.  4.2,  this  configuration  was  used  as  a  starting  point  for  the  seeker

objective design. Also  F# was given. To eliminate Narcissus effect,  (Secondary and

higher reflections between lenses cause some spots on focal plane array) all objective

lenses  are  thought  to  have  antireflection  coatings  instead  of  dome  material.  Dome

material  was  selected  as  a  sapphire  material  because  it  is  durable  to  aerodynamic

effects. Transmission of dome was taken approximately as 0.85 [21]. As a result total

optical  transmission  was  approximately  0.85,  because  lenses  have  antireflection

coatings.

Fig. 4.3 shows interface of the software for infrared range calculation. This software

was programmed in C# and developed codes were given in APPENDIX A. NETD is

the  figure  of  merit  for  IIR  detectors.  From  NETD,  detector  noise  (NEP)  can  be

determined and according to results lock on range can be calculated for given optical

parameters. Left column in Fig. 4.3, NEP was calculated. Calculation was done using

Ågtrapezoidal ruleÅh. NETD is 20 mK, wavelength interval is between 4.9 É m and 3,6

É m spectral region (cold shield spectral region). Background temperature was taken

as 295 K and emissivity was taken 0.98 [19], because MWIR sensors are tested at 22

ÅãC  temperature  background  conditions  and  with  no  optics.  So,  ÅgT  opticsÅh

(Transmission of optics) is equal to 1 and F number of optics is equal 1. Absorbance

of  detector  was  assumed  as  0.6.  (From  literature,  it  is  found that  the  reflectance  of

InSb  material  in  MWIR  region  is  approximately  0.40  [18]).  Using  Eq.  2.16,

ÅgInfrared  Range  and  NETD  CalculatorÅh  software  was  programmed.  Interface  is

shown in Fig. 4.3.

42

DetectorCold Shield HeightCold ShieldWindowMechanical CasefhfF?#h

Figure 4.3 Infrared range and NETD calculator software interface

The NEP of detector is approximately 3.12 x 10-13 W. Signal comes from the target

must greater than the noise of detector and the background radiation.

For detection range calculation, right  column was used which is shown  in Fig. 4.3.

For  lock  on  range  condition,  power  from  target  must  be  greater  than  power  from

background and also NEP of detector.

43

targettargettargettarget....121???????????optatmTTAdMP??????backgroundbackgroundbackgroundbackground....121???????????optatmTTAdMP??????

where

is  area  of  target  and  background,

  is  the  transmission  of  atmosphere,

is transmission of optic, É√ is the emissivity,

 is the spectral radiant exitance in

interval between

and

 and É∂ is the solid angle seen by optics.

Wavelength interval was taken according to cold shield properties (between 3.6 ?m

and 4.9 ?m). F# is a detector property and was taken as 3.

 was taken as 5000

cm2 and

Fig. 4.4;

 was calculated using the geometry for single pixel as shown in

Figure 4.4 Background dimension calculation

where

.  Fig.  4.5  shows  solid  angle  (É∂)  calculations.  For

background  and  target,  same  solid  angle  was  used  because  target  and  background

were assumed as a point source.

44

AatmToptT?M1?2?targetAbackgroundARange 5000 mEFLScene (S)Pixel Pitch (p)Optical SystemmmmmmEFLpRangeSEFLpRangeS36030.5000.??????229)3(mmAbackground??

Figure 4.5 Solid angle calculations.

Transmission of atmosphere was calculated using Eq. 2.1 and extinction coefficient É–
was taken as 5 x 10-6 cm-1 [20].

Focal  length  of  the  optical  system  was  determined  under  those  situations.  Focal

length of the system is 60 mm.

,

 and NEP of detector were calculated

as 3.198 x 10-10 W, 3.647 x 10-12 W and is 3.12 x 10-13 W. Power from background

and NEP values are below the target radiation. As a result detection can be provided.

4.2 Optical Design of Seeker Objective

The spectral region of the optical system is between 3.6 ?m and 4.9 ?m. F# is 3 and

effective focal length was calculated as 60 mm. Fig. 4.6 shows FOV calculation for

the optical system.

45

Point TargetOptical System22#222)2()2(RFEFLRCARA??????RAtargetPbackgroundP

Figure 4.6 FOV calculation for optical system

FOV can be taken as Å}3.7Åã approximately. Optical parameters were summarized in

Table 4.2.

Table 4.2 Optical parameters

Spectral Region

3.6 ?m-4.9?m

EFL

F#

FOV

60 mm

3

Å} 3.7 Åã

Optical Transmission

0.85

Required  effective  focal  length  is  60  mm,  diffraction  limited  spot  diameter  for  3.6

?m wavelength is 26.4 ?m and for 4.9 ?m wavelength 29.3 ?m.

Lens parameters were calculated from Eq. 2.14. and Eq. 2.12, second surface of the

lens with desired effective focal length was derived. The derivation was

                     (4.1)

46

??????????????????)2(2)12()12()2(2)1(2nnnCTnEFLnnR

Using  Eq.  4.1  and  Eq.  2.14  with  8  mm  CT  of  the  single  sapphire  (refractive  index

was taken as 1.7 [23]) lens parameters were calculated. Lens parameters are shown in

Table 4.3. Zemax simulation results are shown in Fig. 4.13 a) shows optical system

configuration  and  Fig.  4.13  b)  shows  spot  sizes  for  different  fields  such  as  0Åã,

Å}3.7Åã, etc.

Distance between Lens1Åfs second surface and Stop point is 39.506 mm. Total length

of the optical system is 66.906 mm.

Table 4.3 Lens parameters for case 1

Material

CT

 (mm)

Lens1

BFL

Sapphire

8

-

58.906

R1

(mm)

43.35

-

R2

 (mm)

646.19

-

Conic

Constant

0

-

47

a)

b)

Figure 4.7 Zemax simulations for case 1; a) optical system, b) spot sizes for
different fields.

As shown in Fig. 4.7 spot diameter of single lens was found approximately 5 mm and

effective focal length of the system was found 68.45 mm. Required spot diameter is

below 30 ?m and effective focal length is 60 mm.

48

Lens1

First  surface,  second  surface  and  BFL  were  optimized  to  desired  effective  focal

length and spot sizes. Results are shown in Fig. 4.8 and Table 4.4.

As shown in Fig. 4.8, effective focal length was reached to desired value (60 mm).

Although  the  spot  size  was  reduced  to  approximately  4  mm,  it  is  not  in  desired

dimensions. Parameters were shown in Table 4.4.

Table 4.4 Lens parameters for case 2

Material

CT

 (mm)

R1

(mm)

R2

Conic

 (mm)

Constant

Lens1

BFL

Sapphire

8

33.061

162.430

-

51.209

-

-

0

-

49

a)

b)

Figure 4.8 Zemax simulations for case 2; a) optical system, b) spot sizes
for different fields.

To  reach  required  values  of  spot  size,  single  sapphire  lens  was  splitted  into  two

lenses.  First  surface  of  Lens1,  second  surface  of  Lens2  and  First  surfaceÅfs  conic

constant  of  Lens1  were  chosen  as  variable  and  optimized  using  ZemaxÅfs

50

Lens1

optimization tool. Optical system and spot sizes for different fields are shown in Fig.

4.9. Lens parameters are given in Table 4.5.

Table 4.5 Lens parameters for case 3

Material

Lens1

Sapphire

Air

-

Lens2

Sapphire

CT

(mm)

8

4

4

R2

(mm)

Conic

Constant

infinity

-0.360 First Surface

R1

(mm)

33.061

-

-

infinity

52.620

-

0

-

BFL

-

42.4

-

-

51

a)

b)

Figure 4.9 Zemax simulations for case 3; a) optical system, b) spot sizes
for different fields.

As  shown  in  Fig.  4.9,  spot  sizes  were  found  about  2  mm  diameter.  So  it  is  not  in

desired values. Using Hammer Optimization, optimization  was done  for  Lens1 and

Lens2. First and second surface of Lens1, first and second surface of Lens2, CT of

Lens1 and Lens2, BFL and first surfaceÅfs conic constant were chosen as variable.

52

Lens1Lens2

Optimized  optical  system  is  shown  in  Fig.  4.10  and  lens  parameters  are  given  in

Table 4.6.

Table 4.6 Lens parameters for case 4

Material

CT

 (mm)

R1

(mm)

R2

(mm)

Conic

Constant

39.945

37.445

-0.135 First Surface

Lens1

Sapphire

Air

Lens2

BFL

-

GaAs

-

2

4

3

-

-

41.798

36.473

-

0

-

55.873

-

-

53

a)

b)

Figure 4.10 Zemax simulations for case 4; a) optical system, b) spot
sizes for different fields.

As shown in Fig. 4.10 spot sizes of the optical system are reached to desired values.

Approximately  they  are  about  50  ?m.  To  reach  desired  values  distance  between

lenses,  BFL,  all  radiuses  of  the  lenses  and  first  surfaceÅfs  conic  constant  of  Lens1

were chosen  as variable and Hammer optimization was  done. Results  are shown in

Fig. 4.11 and Table 4.7.

54

Lens1Lens2

Table 4.7 Lens parameters for case 5

Material

CT

 (mm)

R1

(mm)

R2

(mm)

Conic

Constant

Lens1

ZNS_BROAD

Air

-

Lens2

SILICON

3

1

3

-

-

35.699

55.322

48.200

34.552

-0.054 First Surface

-

0

-

BFL

-

55.27

-

-

55

a)

b)

Figure 4.11 Zemax simulations for case 5; a) optical system, b) spot
sizes for different fields.

As shown Fig. 4.11 b) spot radius of the field zero is below 30 ?m but other fields

are  greater  than  30  ?m.  Optical  system  has  coma  aberration  as  shown  in  Fig.  4.11

spot sizes. In MWIR systems, spot positions are constant and an extra lens must be

added to the system to get rid of the coma aberration.

56

Lens1Lens2

To reach desired values, distances between lenses, BFL, all radiuses of the lenses, all

CT  of  lenses,  second  surfaceÅfs  conic  constant  of  Lens2  and  first  surfaceÅfs  conic

constant  of  Lens3  were  chosen  as  variable  and  Hammer  optimization  was  done.

Results are shown in Fig. 4.12 and Table 4.8.

Table 4.8 Lens parameters for case 6

Material

Lens1

GE_OLD

Air

-

Lens2

SILICON

Air

Lens3

BFL

-

CDSE

-

CT

 (mm)

2.822

2

4.042

36.15

3.583

21.4

R1

(mm)

39.528

-

R2

(mm)

31.783

-

Conic

Constant

0

-

34.352

53.759

0.043 Second Surface

-

-

-

49.178

56.378

-5.833 First Surface

-

-

-

57

a)

b)

Figure 4.12 Zemax simulations for case 6 ; a) optical system, b) spot
sizes for different fields.

As shown Fig. 4.12 b) all spots are almost in desired values. They are below 30 ?m

pixel  pitch.  Dome  material  should  be  sapphire  because  of  the  aerodynamic  effects

that acts on dome such as thermal, acceleration. The dome must be durable to these

effects.  As  a  result  dome  material  was  chosen  as  a  sapphire  and  Hammer

optimization was done.

58

Lens1Lens2Lens3

Dimensions  of  dome  must  be  compatible  with  missile  diameter.  The  diameter  of

missile was assumed as 140 mm before. So that first surface radius of the dome must

be 70 mm and according to chosen thick second surface radius must be first surface

radius mines thickness. Results are shown in Fig. 4.13 and Table 4.9.

Material

Dome

Sapphire

Air

-

Table 4.9 Lens parameters for case 7

CT

 (mm)

2

2

R1

(mm)

70

-

R2

(mm)

68

-

Lens1

GE_OLD

2.956

38.254

31.104

Conic

Constant

0

-

0

-

Air

-

Lens2

SILICON

Air

Lens3

BFL

-

CDSE

-

2

3.922

33.72

2.001

21.4

-

-

33.253

51.532

0.088 Second Surface

-

-

-

61.932

69.817

-15.917 First Surface

-

-

-

59

a)

b)

Figure 4.13 Zemax simulations for case 7; a) optical system, b)

spot sizes for different fields.

As  in  Fig.  4.13  and  Table  4.9  dome  does  not  have  significant  effect  on  optical

system. Optical system has reached desired values with dome.

4.3 Optical System Performance Parameters

According Rayleigh criteria for aberrations except distortion must below 0.25É… for a

good  imaging  system  [15].  Parameters  are  shown  in  Fig.  4.14.  For  0Åã  field,

60

Lens1Lens2Lens3Dome

aberrations are below 0.1 É…, for 3Åã field aberrations below 0.05 É… and for 3.7Åã field

aberrations are below 0.1 É….

61

a)

b)

c)

Figure 4.14 OPD of the optical system a) 0Åã field, b) 3Åã field
and c) 3.7Åã field

62

Distortion  figures  are  shown  in  Fig.  4.15.  For  3.6  ?m  wavelength,  distortion  is  %

0.4856  and  for  4.9  ?m  wavelength  distortion  is  %  0.4841.  They  are  below  %  2

distortion  criteria  and  distortion

is  positive  both  maximum  and  minimum

wavelengths.

63

a)

b)

Figure 4.15 Distortion of the optical system

64

MTF  is  the  most  important  system  performance  criteria  for  an  optical  system.  It

shows how the optical system performs between scene and detector.

As  shown  Fig.  4.16  a)  0.76  portion  of  target  and  background  signal  will  be

transferred  to  the  detector.  If  the  background  radiation  is  neglected,  because

, 0.76 portion of target signal will pass. MTF was calculated for

one  black  line,  means  minimum  intensity  and  for  one  white  line,  means  maximum

intensity. Calculation is ?*0.030mm=16.67line/mm.

MTF value below 0.1, optical system does not give an image of scene. This critical

value was found from the graph as shown in Fig. 4.16.

65

backgroundPP??target

a)

b)

Figure 4.16 MTF of the optical system

66

16.670.76730.1

   CHAPTER 5

5. DISCUSSION AND CONCLUSION

In  this  study,  imaging  infrared  seeker  was  designed.  Firstly,  spectral  band  of  the

system was analyzed. Since target was chosen as an aircraft and target temperature

was 750 K, the spectral band of the system was taken as MWIR. Atmospheric effects

are  found  from  literature  because  there  was  no  chance  to  make  modeling  with

MODTRAN  software.  Therefore,  MWIR  detector  parameters  were  provided  from

off-the-shelf  products.  Then,  detection  range  equations  for  5000  m  distance  were

determined considering 750 K target radiation and 283 K background radiation and

these equations were programmed with C# programming language.

After  detection  range  calculations,  optical  system  parameters  and  performance

criterions were defined. Focal length of the system was calculated as 60 mm and F#

is below 3. Resolution criterion in focal plane is detector pixel size.

While doing this optical design Zemax software was used. Merit function editor was

used to restrict the optical system such as 60 mm focal plane, 70 mm total length, etc,

while  doing  optimization  and  Hammer  optimization.  Simulations  of  optical  system

were done for different fields.

To  obtain  near  diffraction  limited  system,  4  different  types  of  glass  were  used.

Sapphire  is  dome  material  and  it  was  not  optimized.  For  Lens1,  Ge_Old  lens  was

used. For Lens2, Silicon lens was used and for Lens3, CdSe lens material was used.

These  material  types  were  determined  while  Hammer  optimization.  Before

67

optimization,  usable  infrared  materials  must  be  determined  because  some  lens

materials cause problems. For example NaCl glass melts under moist conditions.

OPD plots were drawn for different fields and for different wavelength. The optical

system  satisfies  the  Rayleigh  resolution  criterion  and  distortion  is  below  %2  for

maximum and minimum wavelength.

To  manufacture  of  this  optics  test  plate  fitting  must  be  done  to  be  manufactured

company.  ÅgEdmund  Optics  Inc.Åh  is  chosen  to  test  the  manufacturability.  Test  plate

fitted parameters are shown in Table 5.1.

Table 5.1 Lens parameters after test plate fitting

Material

CT

R1

R2

Conic

 (mm)

(mm)

(mm)

Constant

Dome

Sapphire

Air

-

2

2

70

-

68

-

Lens1  GE_OLD

2.956

38.354

31.318

Air

-

2

-

-

0

-

0

-

Lens2

SILICON

3.922

33.350

51.460

Air

-

33.72

-

-

Lens3

CDSE

2.001

61.849

69.790

BFL

-

21.4

-

-

0.088 Second

Surface

-

-15.917 First

Surface

-

OPD  for  0Åã  field,  aberrations  are  below  0.1  É…,  for  3Åã  field  aberrations  below  0.1  É…

and for 3.7Åã field, aberrations are below 0.1 É…. Only difference comes from 3Åã field.

But it is again below the Rayleigh criteria.

Distortion is %0.4722 for 3.6 ?m and %0.4705 for 4.9 ?m.

MTF is 0.76. It is same before test plate fitting.

68

Space  is  limited  with  the  missile  diameter.  SeekerÅfs  optics  must  be  settled  in  this

geometry. As a result, total length of the seekerÅfs optics must not exceed 70 mm for

140 mm diameter missile.

To sum  up, imaging infrared seeker  analysis was  done for aerial  targets  at 5000 m

distance. Test plate fitted configuration is convenient to manufacture because system

performance does not degrade significantly. It satisfies system requirements after all.

Although  the  results  presented  here  is  effective,  for  more  cost  effective  solution  of

the  seeker  optics,  optimization  processes  can  be  repeated.  Manufacturing  coast  can

be reduced because the seeker is one of the high-priced parts of a missile.

69

70

REFERENCES

1.  Bruce H. Walker, Optical Engineering Fundamentals, SPIE Press, 2008,

pp 112-113.

2.  Canada Research Chair

http://mivim.gel.ulaval.ca/dynamique/index.php?idD=58&Lang=1
Retrieved on 13 October 2013

3.  Arnold Daniels,  Field Guide to Infrared Systems, SPIE Press, 2007, pp 1-

50

4.  Aerospaceweb.org

http://www.aerospaceweb.org/question/electronics/q0191.shtml
Retrieved on 16 January 2014

5.  Helmut  Budzier  and  Gerald  Gerlach,  Thermal  Infrared  Sensors  Theory

Optimisation and Practice, WILEY, Germany, 2011, pp 117-121

6.  A.  Rogalski  and  K.  Chrzanowski,  ÅgInfrared  Devices  and  TechniquesÅh,

Opto-Electronics Review, 2002, Vol. 10, pp 111-136

7.  Bakshi,  U.  A.  and  Godse,  A.  P.  Basic  Electronics  Engineering,  2009,

Technical Publications. pp. 8?10.

8.  Song,  T.L,  ÅgTarget  Adaptive  Guidance  for  Passive  Homing  MissilesÅh,

1997, IEEE, Vol. 33, Issue 1, pp 312-316.

9.  David  H.  Pollock,  The  Infrared  &  Electro-Optical  Systems  Handbook,

Countermeasure Systems, Vol. 7, 1999.

10. Shripad  P.  Mahulikar,  Hemant  R.  Sonawane,  G.  Arvind  Rao  ÅgInfrared
Signature Studies of Aerospace VehiclesÅh, 2007, Science Direct, Vol. 43,
Issue 7-8, pp 218-245.

71

11. Sang-Ho  Ahn,  Young-Choon  Kim,  Tae-Wuk  Bae,  Byoung-Ik  Kim,  Ki-
Hong  Kim,  ÅgDIRCM  Jamming  Effect  Analysis  of  Spin-Scan  Reticle
SeekerÅh, Communications (MICC), 2009 IEEE 9th Malaysia International
Conference on, pp 183-186.

12. Tae-Wuk  Bae,  Byoung-Ik  Kim,  Young-Choon  Kim,  Sang-Ho  Ahn,
ÅgJamming  effect  analysis  of  infrared  reticle  seeker  for  directed  infrared
countermeasuresÅh, 2012,  Infrared Physics & Technology, Vol. 55,  Issue
5, pp 431?441.

13. Surng-Gabb  Jahng,  Hyun-Ki  Hong,  Sung-Hyun  Han,  Jong-Soo  Choi,
ÅgDynamic  simulation  of  the  rosette  scanning  infrared  seeker  and  an
infrared  counter  countermeasure  using  the  moment  techniqueÅh,  1998,
SPIE Optical Engineering, Vol. 38, Issue 5, pp 921-928.

14. Ehsan  Rahimi,  Shahriar  B.  Shokouhi,  ÅgA  Parallelized  and  Pipelined
Datapath to Implement ISODATA Algorithm for Rosette Scan Images on
a Reconfigurable HardwareÅh, 2007, IEEE, p 433.

15. Robert  E.  Fischer,  Biljana  Tadic-Galeb,  Paul  R.  Yoder,  Optical  System

Design, Second Edition, pp 29-90

16. O. Nesher, S. Elkind, G. Francis, M. Kenan,  ÅgSCD Solutions for Missile

Warning SystemsÅh, 2006, SPIE, Vol. 6206

17.  Ajay  Kumar  and  S.S.  Negi  ÅgDesign  and  Development  of  High
Performance  3rd  Generation  Hand  Held  Thermal  CameraÅh,  2004,  SPIE,
Vol. 5563

18. Peter  Y.  Yu  and  Manuel  Cardona,  Fundamentals  of  Semiconductors

Physics and Materials Properties, Springer Press, 2010. p. 310.

19.  Standart  Test  Method  for  Noise  Equivalent  Temperature  Difference  of
Thermal Imaging Systems, ASTM International, Designation E1543-00.

72

20. Ab-Rahman  and  Mazen  R.  Hassan,  Mohammed  Syuhaimi,  ÅgLock-on
Range of Infrared Heat Seeker MissileÅh, 2009, Electrical Engineering and
Informatics, 2009, International Conference on, Vol. 02, pp 472 ? 477.

21. Donald  E.  McCharty  ÅgThe  Reflection  and  Transmission  of  Infrared
Materials: I, Spectra from 2 50 MicronsÅh, Applied Optics, Vol. 2, Issue 6,
pp 591-595.

22. Max J. Riedl, Optical Design Applying the Fundamentals, SPIE, 2009.

23. Robert  E.  Fischer,  R.  Barry  Johnson,  Warren  J.  Smith  ÅgScalable  MWIR
and  LWIR  optical  system  designs  employing  a  large  spherical  primary
mirror  and  small  refractive  aberration  correctorsÅh  2001,  SPIE,  Vol.
4441.

73

74

APPENDIX A

SOFTWARE CODES OF ÅgINFRARED RANGE AND NETD

CALCULATORÅh

ÅgInfrared Range and NETD CalculatorÅh software programming (C#) codes;

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace NETD
{
    public partial class Form1 : Form
    {

        double NETD;
        double lambda2;
        double lambda1;
        double Toptics;
        double PixelPitch;
        double FNumber;
        double EmissivityBack;
        double Tbackground;
        double NEP;
        double CalculationSensitivity;
        double DetectorAbsorbtion;

        // constants;

        double h;
        double k;
        double c;

        // Detection Range

        double DetectionRange;
        double ExtinctionCoefficient;
        double TargetArea;
        double BackgroundArea;
        double TargetTemperature;
        double TargetEmissivity;

75

        double BackTemperature;
        double BackEmissivity
        double FocalLength;
        double AtmosphericTrans;
        double ClearAperture;
        double PowOnDetTarget;
        double PowOnDetBack;

        public Form1()
        {
            InitializeComponent();
            h = 6.62606957 * Math.Pow(10, -34); // J.s
            c = 3 * Math.Pow(10, 8); // m/s
            k = 1.3806488 * Math.Pow(10, -23);  //  J/K
        }

        private void button1_Click(object sender, EventArgs e)
        {
            NETD = double.Parse(textBox1.Text) * Math.Pow(10, -3);
            lambda2 = double.Parse(textBox3.Text) * Math.Pow(10, -6);
            lambda1 = double.Parse(textBox4.Text) * Math.Pow(10, -6);
            Tbackground = double.Parse(textBox5.Text) ;
            Toptics = double.Parse(textBox6.Text);
            PixelPitch = double.Parse(textBox7.Text) * Math.Pow(10, -6);
            FNumber = double.Parse(textBox8.Text);
            EmissivityBack = double.Parse(textBox9.Text);
            CalculationSensitivity = double.Parse(textBox10.Text);
            DetectorAbsorbtion = double.Parse(textBox11.Text);
            NEP = NETD * DerivativeExitanceCalculator(Tbackground, lambda2,
lambda1, EmissivityBack, CalculationSensitivity, DetectorAbsorbtion) *
Math.Pow(PixelPitch, 2) * Toptics / (4 * Math.Pow(FNumber, 2) + 1);
            textBox2.Text = NEP.ToString();
        }

        public double DerivativeExitanceCalculator(double Temperature, double
Lambda2, double Lambda1, double emissivity, double Sensitivity, double
Absorbtion)
        {
            double h = 6.62606957 * Math.Pow(10, -34); // J.s
            double c = 3 * Math.Pow(10, 8); // m/s
            double k = 1.3806488 * Math.Pow(10, -23);  //  J/K
            double[] Lambda;
            double[] sabit;
            double[] fonk;
            double integral = 0;
            int ArrayLength = Convert.ToInt32((lambda2 - lambda1) *
Math.Pow(10, 6) * Sensitivity) + 1;
            Lambda = new double[ArrayLength];
            sabit = new double[ArrayLength];
            fonk = new double[ArrayLength];
            Lambda[0] = lambda1;
            for (int i = 1; i < Lambda.Length ; i++)
            {
                Lambda[i] = Lambda[0] + (double)i * (lambda2 - lambda1) /
Lambda.Length;
            }

76

            for (int i = 0; i < Lambda.Length ; i++)
            {
                sabit[i] = h * c / (Lambda[i] * k * Temperature);
            }
            for (int i = 0; i < Lambda.Length ; i++)
            {
                fonk[i] = emissivity * Absorbtion * (2 * Math.PI * Math.Pow(h,
2) * Math.Pow(c, 3) / (Math.Pow(Lambda[i], 6) * k * Math.Pow(Temperature, 2))
* Math.Exp(sabit[i]) / (Math.Pow((Math.Exp(sabit[i]) - 1), 2)));
            }
            for (int i = 0; i < Lambda.Length-1; i++)
            {
                integral = integral + (Lambda[i + 1] - Lambda[i]) * (fonk[i +
1] + fonk[i]) / 2;
            }
            return integral;
        }

        public double SpectralRadianceExitance(double lambda2, double lambda1,
double Temperature, double emissivity, double Sensitivity)
        {
            /// (W/m2-É m)
            double h = 6.62606957 * Math.Pow(10, -34); // J.s
            double c = 3 * Math.Pow(10, 8); // m/s
            double k = 1.3806488 * Math.Pow(10, -23);  //  J/
            double[] Lambda;
            double[] sabit;
            double[] fonk;
            double integral = 0;
            int ArrayLength = Convert.ToInt32((lambda2 - lambda1) *
Math.Pow(10, 6) * Sensitivity) + 1;
            Lambda = new double[ArrayLength];
            sabit = new double[ArrayLength];
            fonk = new double[ArrayLength];
            Lambda[0] = lambda1;
            for (int i = 1; i < Lambda.Length; i++)
            {
                Lambda[i] = Lambda[0] + (double)i * (lambda2 - lambda1) /
Lambda.Length;
            }
            for (int i = 0; i < Lambda.Length; i++)
            {
                sabit[i] = h * c / (Lambda[i] * k * Temperature);
            }
            for (int i = 0; i < Lambda.Length; i++)
            {
                fonk[i] = emissivity * 2 * Math.PI * h * Math.Pow(c, 2) /
(Math.Pow(Lambda[i], 5) * (Math.Exp(sabit[i])-1));
            }
            for (int i = 0; i < Lambda.Length - 1; i++)
            {
                integral = integral + (Lambda[i + 1] - Lambda[i]) * (fonk[i +
1] + fonk[i]) / 2;
            }
            return integral;
        }

77

        private void button2_Click(object sender, EventArgs e)
        {
            CalculationSensitivity = double.Parse(textBox20.Text);
            DetectionRange = double.Parse(textBox23.Text);
            ExtinctionCoefficient = double.Parse(textBox21.Text) * 100 *
Math.Pow(10, -6);
            TargetArea = double.Parse(textBox24.Text);
            BackgroundArea = double.Parse(textBox25.Text);
            TargetTemperature = double.Parse(textBox22.Text);
            TargetEmissivity = double.Parse(textBox12.Text);
            BackTemperature = double.Parse(textBox13.Text);
            BackEmissivity = double.Parse(textBox14.Text);
            FocalLength = double.Parse(textBox15.Text)/1000;
            lambda2 = double.Parse(textBox27.Text) * Math.Pow(10, -6);
            lambda1 = double.Parse(textBox26.Text) * Math.Pow(10, -6);
            FNumber = double.Parse(textBox17.Text);
            DetectorAbsorbtion=double.Parse(textBox29.Text);
            AtmosphericTrans = Math.Exp(-ExtinctionCoefficient *
DetectionRange);
            ClearAperture = FocalLength / FNumber;
            PowOnDetTarget = DetectorAbsorbtion *
SpectralRadianceExitance(lambda2, lambda1, TargetTemperature,
TargetEmissivity, CalculationSensitivity) * TargetArea *
                Math.Pow(ClearAperture / 2, 2) * Toptics * AtmosphericTrans /
Math.Pow(DetectionRange, 2);
            PowOnDetBack =DetectorAbsorbtion *
SpectralRadianceExitance(lambda2, lambda1, BackTemperature, BackEmissivity,
CalculationSensitivity) *
                BackgroundArea * Math.Pow(ClearAperture / 2, 2) * Toptics *
AtmosphericTrans / Math.Pow(DetectionRange, 2);
            textBox18.Text = PowOnDetTarget.ToString();
            textBox19.Text = PowOnDetBack.ToString();
            textBox28.Text = NEP.ToString();
            textBox30.Text = Math.Round((PowOnDetTarget / NEP),3).ToString();
            textBox16.Text = Math.Round((PowOnDetBack / NEP),3).ToString();
            textBox31.Text = (SpectralRadianceExitance(lambda2, lambda1,
TargetTemperature, TargetEmissivity, CalculationSensitivity) /
SpectralRadianceExitance(lambda2, lambda1, BackTemperature, BackEmissivity,
CalculationSensitivity)) .ToString();
            led1.Value = true;
        }
    }
}

78


