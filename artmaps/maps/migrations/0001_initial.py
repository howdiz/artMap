# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('maps_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('hood', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('septa', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('maps', ['Location'])

        # Adding model 'Gallery'
        db.create_table('maps_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Location'])),
            ('advertiser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blog_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('gallery_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('maps', ['Gallery'])

        # Adding model 'Show'
        db.create_table('maps_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Gallery'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('artist', self.gf('django.db.models.fields.TextField')(max_length=550, blank=True)),
            ('blog_link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('opening_date', self.gf('django.db.models.fields.DateField')()),
            ('time_info', self.gf('django.db.models.fields.TextField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pick', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=550)),
        ))
        db.send_create_signal('maps', ['Show'])

        # Adding model 'Event'
        db.create_table('maps_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Gallery'])),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=550)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('multiday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timeInfo', self.gf('django.db.models.fields.TextField')(max_length=250, blank=True)),
            ('admission', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('pick', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('maps', ['Event'])


    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('maps_location')

        # Deleting model 'Gallery'
        db.delete_table('maps_gallery')

        # Deleting model 'Show'
        db.delete_table('maps_show')

        # Deleting model 'Event'
        db.delete_table('maps_event')


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
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'opening_date': ('django.db.models.fields.DateField', [], {}),
            'pick': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'time_info': ('django.db.models.fields.TextField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['maps']
