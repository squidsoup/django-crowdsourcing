# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table('crowdsourcing_survey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('tease', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thanks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('require_login', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_multiple_submissions', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('moderate_submissions', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_voting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('archive_policy', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('starts_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('survey_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ends_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sections', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sections', null=True, to=orm['crowdsourcing.Section'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('flickr_group_id', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('flickr_group_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default_report', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='reports', null=True, to=orm['crowdsourcing.SurveyReport'])),
        ))
        db.send_create_signal('crowdsourcing', ['Survey'])

        # Adding unique constraint on 'Survey', fields ['survey_date', 'slug']
        db.create_unique('crowdsourcing_survey', ['survey_date', 'slug'])

        # Adding model 'Question'
        db.create_table('crowdsourcing_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['crowdsourcing.Survey'])),
            ('fieldname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('label', self.gf('django.db.models.fields.TextField')()),
            ('help_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='question_section', null=True, to=orm['crowdsourcing.Section'])),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('option_type', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('numeric_is_int', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('options', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('map_icons', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('answer_is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('use_as_filter', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('crowdsourcing', ['Question'])

        # Adding unique constraint on 'Question', fields ['fieldname', 'survey']
        db.create_unique('crowdsourcing_question', ['fieldname', 'survey_id'])

        # Adding model 'Section'
        db.create_table('crowdsourcing_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='survey', to=orm['crowdsourcing.Survey'])),
        ))
        db.send_create_signal('crowdsourcing', ['Section'])

        # Adding model 'Submission'
        db.create_table('crowdsourcing_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdsourcing.Survey'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('submitted_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('session_key', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('crowdsourcing', ['Submission'])

        # Adding model 'Answer'
        db.create_table('crowdsourcing_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdsourcing.Submission'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdsourcing.Question'])),
            ('text_answer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_answer', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('integer_answer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('float_answer', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('boolean_answer', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('image_answer', self.gf('django.db.models.fields.files.ImageField')(max_length=500, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flickr_id', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('photo_hash', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal('crowdsourcing', ['Answer'])

        # Adding model 'SurveyReport'
        db.create_table('crowdsourcing_surveyreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdsourcing.Survey'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sort_by_rating', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('display_the_filters', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('limit_results_to', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('display_individual_results', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('crowdsourcing', ['SurveyReport'])

        # Adding unique constraint on 'SurveyReport', fields ['survey', 'slug']
        db.create_unique('crowdsourcing_surveyreport', ['survey_id', 'slug'])

        # Adding model 'SurveyReportDisplay'
        db.create_table('crowdsourcing_surveyreportdisplay', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdsourcing.SurveyReport'])),
            ('display_type', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('aggregate_type', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('fieldnames', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('x_axis_fieldname', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('annotation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('limit_map_answers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('map_center_latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('map_center_longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('map_zoom', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('caption_fields', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('crowdsourcing', ['SurveyReportDisplay'])


    def backwards(self, orm):
        # Removing unique constraint on 'SurveyReport', fields ['survey', 'slug']
        db.delete_unique('crowdsourcing_surveyreport', ['survey_id', 'slug'])

        # Removing unique constraint on 'Question', fields ['fieldname', 'survey']
        db.delete_unique('crowdsourcing_question', ['fieldname', 'survey_id'])

        # Removing unique constraint on 'Survey', fields ['survey_date', 'slug']
        db.delete_unique('crowdsourcing_survey', ['survey_date', 'slug'])

        # Deleting model 'Survey'
        db.delete_table('crowdsourcing_survey')

        # Deleting model 'Question'
        db.delete_table('crowdsourcing_question')

        # Deleting model 'Section'
        db.delete_table('crowdsourcing_section')

        # Deleting model 'Submission'
        db.delete_table('crowdsourcing_submission')

        # Deleting model 'Answer'
        db.delete_table('crowdsourcing_answer')

        # Deleting model 'SurveyReport'
        db.delete_table('crowdsourcing_surveyreport')

        # Deleting model 'SurveyReportDisplay'
        db.delete_table('crowdsourcing_surveyreportdisplay')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crowdsourcing.answer': {
            'Meta': {'ordering': "('question',)", 'object_name': 'Answer'},
            'boolean_answer': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date_answer': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'float_answer': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_answer': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'blank': 'True'}),
            'integer_answer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'photo_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourcing.Question']"}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourcing.Submission']"}),
            'text_answer': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'crowdsourcing.question': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('fieldname', 'survey'),)", 'object_name': 'Question'},
            'answer_is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fieldname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'map_icons': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'numeric_is_int': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'option_type': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'options': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'question_section'", 'null': 'True', 'to': "orm['crowdsourcing.Section']"}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['crowdsourcing.Survey']"}),
            'use_as_filter': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'crowdsourcing.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'survey'", 'to': "orm['crowdsourcing.Survey']"})
        },
        'crowdsourcing.submission': {
            'Meta': {'ordering': "('-submitted_at',)", 'object_name': 'Submission'},
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'submitted_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourcing.Survey']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'crowdsourcing.survey': {
            'Meta': {'ordering': "('-starts_at',)", 'unique_together': "(('survey_date', 'slug'),)", 'object_name': 'Survey'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_multiple_submissions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_voting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'archive_policy': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'default_report': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports'", 'null': 'True', 'to': "orm['crowdsourcing.SurveyReport']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ends_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'flickr_group_id': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'flickr_group_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderate_submissions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'require_login': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sections': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sections'", 'null': 'True', 'to': "orm['crowdsourcing.Section']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'survey_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'tease': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thanks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'crowdsourcing.surveyreport': {
            'Meta': {'ordering': "('title',)", 'unique_together': "(('survey', 'slug'),)", 'object_name': 'SurveyReport'},
            'display_individual_results': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'display_the_filters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_results_to': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sort_by_rating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourcing.Survey']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'crowdsourcing.surveyreportdisplay': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SurveyReportDisplay'},
            'aggregate_type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'annotation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'caption_fields': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'display_type': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fieldnames': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_map_answers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'map_center_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'map_center_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'map_zoom': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourcing.SurveyReport']"}),
            'x_axis_fieldname': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['crowdsourcing']