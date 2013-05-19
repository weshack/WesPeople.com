# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'maps_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('page_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('wesleyan_degree_school_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('wesleyan_degree_year_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('wesleyan_degree_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('wesleyan_degree_1_major_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('wesleyan_degree_1_major_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('wesleyan_degree_1_major_3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('last_name_at_grad', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('preferred_class_year', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('preferred_email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('position_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('position_status', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('business_address_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('business_address_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('business_address_city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('business_address_state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('business_address_zip', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('business_address_country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'maps', ['Person'])

        # Adding model 'AuthUser'
        db.create_table(u'maps_authuser', (
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['maps.Person'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'maps', ['AuthUser'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'maps_person')

        # Deleting model 'AuthUser'
        db.delete_table(u'maps_authuser')


    models = {
        u'maps.authuser': {
            'Meta': {'object_name': 'AuthUser'},
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['maps.Person']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'maps.person': {
            'Meta': {'object_name': 'Person'},
            'business_address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'business_address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'business_address_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'business_address_country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'business_address_state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'business_address_zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name_at_grad': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'mid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'page_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'position_status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'preferred_class_year': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'preferred_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wesleyan_degree_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wesleyan_degree_1_major_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wesleyan_degree_1_major_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wesleyan_degree_1_major_3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'wesleyan_degree_school_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wesleyan_degree_year_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['maps']