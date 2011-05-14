from django.db import models

HOODS = (
	('OC', 'Old City'),
	('CC', 'Center City'),
	('WP', 'West Philly'),
	('NL', 'No Libs'),
	('KN', 'Kens'),
	('HL', 'Hinter Lands'),
	('SP', 'South PHilly')
)

class Location(models.Model):
	nickname = models.CharField(max_length=65)
	address1 = models.CharField(max_length=200)
	address2 = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=5)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True) 
	hood = models.CharField(max_length=25, choices=HOODS)
	septa = models.TextField()
	url = models.CharField(max_length=200) 
	def __unicode__(self):
		return self.nickname
		return self.address
		return self.address2
		return self.city
		return self.state
		return self.zipcode
		return self.latitude
		return self.longitude
		return self.septa
		return self.url 


	    		
class Gallery(models.Model):
	name = models.CharField(max_length=65)
	location = models.ForeignKey(Location)
	advertiser = models.BooleanField()
	blog_url = models.URLField(verify_exists=True, blank=True)
	gallery_url = models.URLField(verify_exists=True, blank=True)
	gallery_hours = models.CharField(max_length=200, blank=True)
	def __unicode__(self):
		return self.name

class Show(models.Model):
	gallery = models.ForeignKey(Gallery)
	name = models.CharField(max_length=100)
	artist = models.TextField(max_length=550, blank=True)
	blog_link = models.URLField(verify_exists=True, blank=True)
	start_date = models.DateField()
	end_date = models.DateField()
	opening_date = models.DateField()
	time_info = models.TextField(max_length=250)
	image = models.ImageField(upload_to="images", blank=True)
	thumbnail = models.ImageField(upload_to="images", blank=True)
	pick = models.BooleanField()
	description = models.TextField(max_length=550)
	def __unicode__(self):
		return self.name
		return self.artist
		return self.blog_link
		return self.description

EVENTTYPES = (
('Workshop','Workshop'), ('Performance', 'Performance'), ('Lecture', 'Lecture'), ('Social','Social'),('ArtSale','Art Sale'),('Educatin','Education'), ('Screening','Screening'),('ArtistTalk', 'Artist Talk')
)

class Event(models.Model):
	gallery = models.ForeignKey(Gallery)
	title = models.TextField(max_length=50)
	description = models.TextField(max_length=550)
	image = models.ImageField(upload_to="images", blank=True)
	thumbnail = models.ImageField(upload_to="images", blank=True)
	event_type = models.CharField(max_length=50, choices=EVENTTYPES)
	date = models.DateField()
	start_time = models.TimeField(blank=True)
	end_time = models.TimeField(blank=True)
	multiday = models.BooleanField()
	timeInfo = models.TextField (max_length=250, blank=True)
	admission = models.CharField(max_length=25, blank=True)
	pick = models.BooleanField()
	def __unicode__(self):
		return self.title
		return self.description
		return self.event_type
		return self.timeInfo	
