# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Show.end_date'
        db.alter_column('maps_show', 'end_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Show.start_date'
        db.alter_column('maps_show', 'start_date', self.gf('django.db.models.fields.DateField')())


    def backwards(self, orm):
        
        # Changing field 'Show.end_date'
        db.alter_column('maps_show', 'end_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Show.start_date'
        db.alter_column('maps_show', 'start_date', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'maps.event': {
            'Meta': {'object_name': 'Event'},
            'admission': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '550'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'multiday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pick': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'timeInfo': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '50'})
        },
        'maps.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'advertiser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blog_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'gallery_hours': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gallery_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '65'})
        },
        'maps.location': {
            'Meta': {'object_name': 'Location'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hood': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'septa': ('django.db.models.fields.TextField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'maps.show': {
            'Meta': {'object_name': 'Show'},
            'artist': ('django.db.models.fields.TextField', [], {'max_length': '550', 'blank': 'True'}),
            'blog_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '550'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'opening_date': ('django.db.models.fields.DateField', [], {}),
            'pick': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'time_info': ('django.db.models.fields.TextField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['maps']
