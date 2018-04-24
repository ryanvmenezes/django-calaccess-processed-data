# Generated by Django 2.0.4 on 2018-04-24 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed_filings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form496Filing',
            fields=[
                ('date_filed', models.DateField(db_index=True, help_text='Date this report was filed, according to the filer (from CVR_CAMPAIGN_DISCLOSURE.RPT_DATE)', verbose_name='date filed')),
                ('filer_id', models.IntegerField(db_index=True, help_text='Numeric filer identification number (from FILER_XREF.FILER_ID)', verbose_name='filer id')),
                ('filer_lastname', models.CharField(help_text='Last name of filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAML)', max_length=200, verbose_name='filer last name')),
                ('filer_firstname', models.CharField(blank=True, help_text='First name of the filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAMF)', max_length=45, verbose_name='filer first name')),
                ('election_date', models.DateField(db_index=True, help_text='Date of the election in which the filer is participating (from CVR_CAMPAIGN_DISCLOSURE.ELECT_DATE)', null=True, verbose_name='election date')),
                ('filing_id', models.IntegerField(help_text='Unique identification number for the Schedule 496 filing (from CVR_CAMPAIGN_DISCLOSURE_CD.FILING_ID)', primary_key=True, serialize=False, verbose_name='filing id')),
                ('amendment_count', models.IntegerField(help_text='Number of amendments to the Schedule 496 filing (from maximum value of CVR_CAMPAIGN_DISCLOSURE_CD.AMEND_ID)', verbose_name='Count amendments')),
            ],
            options={
                'verbose_name': 'Form 496 (Late Independent Expenditure) filing',
            },
        ),
        migrations.CreateModel(
            name='Form496FilingVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_filed', models.DateField(db_index=True, help_text='Date this report was filed, according to the filer (from CVR_CAMPAIGN_DISCLOSURE.RPT_DATE)', verbose_name='date filed')),
                ('filer_id', models.IntegerField(db_index=True, help_text='Numeric filer identification number (from FILER_XREF.FILER_ID)', verbose_name='filer id')),
                ('filer_lastname', models.CharField(help_text='Last name of filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAML)', max_length=200, verbose_name='filer last name')),
                ('filer_firstname', models.CharField(blank=True, help_text='First name of the filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAMF)', max_length=45, verbose_name='filer first name')),
                ('election_date', models.DateField(db_index=True, help_text='Date of the election in which the filer is participating (from CVR_CAMPAIGN_DISCLOSURE.ELECT_DATE)', null=True, verbose_name='election date')),
                ('amend_id', models.IntegerField(help_text='Identifies the version of the Schedule 496 filing, with 0 representing the initial filing (from CVR_CAMPAIGN_DISCLOSURE_CD.AMEND_ID)')),
                ('filing', models.ForeignKey(db_constraint=False, help_text='Unique identification number for the Schedule 496 filing (from S496_CD.FILING_ID)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='versions', to='calaccess_processed_filings.Form496Filing')),
            ],
            options={
                'verbose_name': 'Form 496 (Late Independent Expenditure) filing version',
            },
        ),
        migrations.AlterIndexTogether(
            name='form496filing',
            index_together={('filing_id', 'amendment_count')},
        ),
        migrations.AlterUniqueTogether(
            name='form496filingversion',
            unique_together={('filing', 'amend_id')},
        ),
        migrations.AlterIndexTogether(
            name='form496filingversion',
            index_together={('filing', 'amend_id')},
        ),
    ]
