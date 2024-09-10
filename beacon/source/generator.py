from beacon.source.entry_types import analysis, biosample, cohort, dataset, individual, genomicVariant, run
from beacon.source.manage import analyses, biosamples, cohorts, datasets, individuals, g_variants, runs

def get_entry_types(self):
    entry_types={}
    entry_types["entryTypes"]={}
    if analyses["granularity"]["boolean"]==True or analyses["granularity"]["count"]==True or analyses["granularity"]["record"]==True:
        entry_types["entryTypes"]["analysis"]=analysis
    if biosamples["granularity"]["boolean"]==True or biosamples["granularity"]["count"]==True or biosamples["granularity"]["record"]==True:
        entry_types["entryTypes"]["biosample"]=biosample
    if cohorts["granularity"]["boolean"]==True or cohorts["granularity"]["count"]==True or cohorts["granularity"]["record"]==True:
        entry_types["entryTypes"]["cohort"]=cohort
    if datasets["granularity"]["boolean"]==True or datasets["granularity"]["count"]==True or datasets["granularity"]["record"]==True:
        entry_types["entryTypes"]["dataset"]=dataset
    if g_variants["granularity"]["boolean"]==True or g_variants["granularity"]["count"]==True or g_variants["granularity"]["record"]==True:
        entry_types["entryTypes"]["genomicVariant"]=genomicVariant
    if individuals["granularity"]["boolean"]==True or individuals["granularity"]["count"]==True or individuals["granularity"]["record"]==True:
        entry_types["entryTypes"]["individual"]=individual
    if runs["granularity"]["boolean"]==True or runs["granularity"]["count"]==True or runs["granularity"]["record"]==True:
        entry_types["entryTypes"]["run"]=run
    return entry_types