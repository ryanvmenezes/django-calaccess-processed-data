# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-06 01:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0016_auto_20180406_0102'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OCDBallotMeasureContestIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDBallotMeasureContestOptionProxy',
        ),
        migrations.DeleteModel(
            name='OCDBallotMeasureContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDBallotMeasureContestSourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidacyProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidacySourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidateContestPostProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidateContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidateContestSourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDElectionIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDElectionProxy',
        ),
        migrations.DeleteModel(
            name='OCDElectionSourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDPartyProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestOptionProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestSourceProxy',
        ),
    ]