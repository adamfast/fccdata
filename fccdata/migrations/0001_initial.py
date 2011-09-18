# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'en'
        db.create_table('fcc_en', (
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('unique_system_identifier', self.gf('django.db.models.fields.IntegerField')(null=True, primary_key=True)),
            ('uls_file_number', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('ebf_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('call_sign', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('entity_type', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('licensee_id', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('entity_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('mi', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('po_box', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('attention_line', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('sgin', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('frn', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('applicant_type_code', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('applicant_type_code_other', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('status_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('fccdata', ['en'])

        # Adding model 'am'
        db.create_table('fcc_am', (
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('unique_system_identifier', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fccdata.en'], unique=True, null=True, primary_key=True, db_column='unique_system_identifier')),
            ('uls_file_number', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('ebf_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('call_sign', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('operator_class', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('group_code', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('region_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trustee_call_sign', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('trustee_indicator', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('physician_certification', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('ve_signature', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('systematic_call_sign_change', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('vanity_call_sign_change', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('vanity_relationship', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('previous_call_sign', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('previous_operator_class', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('trustee_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('fccdata', ['am'])

        # Adding model 'hd'
        db.create_table('fcc_hd', (
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('unique_system_identifier', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fccdata.en'], unique=True, null=True, primary_key=True, db_column='unique_system_identifier')),
            ('uls_file_number', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('ebf_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('call_sign', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('license_status', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('radio_service_code', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('grant_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('expired_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cancellation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('eligibility_rule_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('alien', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('alien_government', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('alien_corporation', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('alien_officer', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('alien_control', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('revoked', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('convicted', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('adjudged', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('reserved', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('common_carrier', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('non_common_carrier', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('private_comm', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('fixed', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('radiolocation', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('satellite', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('developmental_sta_demonstration', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('interconnected_service', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('certifier_first_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('certifier_mi', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('certifier_last_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('certifier_suffix', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('certifier_title', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('female', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('black_african_american', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('native_american', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('hawaiian', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('asian', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('white', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('hispanic', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('effective_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_action_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('auction_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('broadcast_services_regulatory_status', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('band_manager_regulatory_status', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('broadcast_services_type_of_radio_service', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('alien_ruling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('licensee_name_change', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal('fccdata', ['hd'])


    def backwards(self, orm):
        
        # Deleting model 'en'
        db.delete_table('fcc_en')

        # Deleting model 'am'
        db.delete_table('fcc_am')

        # Deleting model 'hd'
        db.delete_table('fcc_hd')


    models = {
        'fccdata.am': {
            'Meta': {'object_name': 'am', 'db_table': "'fcc_am'"},
            'call_sign': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ebf_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'group_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'operator_class': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'physician_certification': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'previous_call_sign': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'previous_operator_class': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'region_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'systematic_call_sign_change': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'trustee_call_sign': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'trustee_indicator': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'trustee_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'uls_file_number': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'unique_system_identifier': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fccdata.en']", 'unique': 'True', 'null': 'True', 'primary_key': 'True', 'db_column': "'unique_system_identifier'"}),
            'vanity_call_sign_change': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'vanity_relationship': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            've_signature': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'fccdata.en': {
            'Meta': {'object_name': 'en', 'db_table': "'fcc_en'"},
            'applicant_type_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'applicant_type_code_other': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'attention_line': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'call_sign': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ebf_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'entity_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'frn': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'licensee_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'mi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'po_box': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'sgin': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'status_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'uls_file_number': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'unique_system_identifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'primary_key': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'fccdata.hd': {
            'Meta': {'object_name': 'hd', 'db_table': "'fcc_hd'"},
            'adjudged': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'alien': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'alien_control': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'alien_corporation': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'alien_government': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'alien_officer': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'alien_ruling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'asian': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'auction_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'band_manager_regulatory_status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'black_african_american': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'broadcast_services_regulatory_status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'broadcast_services_type_of_radio_service': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'call_sign': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cancellation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'certifier_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'certifier_last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'certifier_mi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'certifier_suffix': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'certifier_title': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'common_carrier': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'convicted': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'developmental_sta_demonstration': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'ebf_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'effective_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'eligibility_rule_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'expired_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'female': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'fixed': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'grant_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hawaiian': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'hispanic': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'interconnected_service': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'last_action_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'license_status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'licensee_name_change': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'native_american': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'non_common_carrier': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'private_comm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'radio_service_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'radiolocation': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'reserved': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'revoked': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'satellite': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'uls_file_number': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'unique_system_identifier': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fccdata.en']", 'unique': 'True', 'null': 'True', 'primary_key': 'True', 'db_column': "'unique_system_identifier'"}),
            'white': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fccdata']
