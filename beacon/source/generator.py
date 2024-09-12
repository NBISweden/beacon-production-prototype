from beacon.source.entry_types import analysis, biosample, cohort, dataset, individual, genomicVariant, run
from beacon.source.manage import analyses, biosamples, cohorts, datasets, individuals, g_variants, runs
from beacon.source.map_entry_types import map_analysis, analysis_single, analysis_genomicVariant, map_biosample, biosample_analysis, biosample_genomicVariant, biosample_run, biosample_single, map_cohort, cohort_analysis, cohort_individual, cohort_run, cohort_single, map_dataset, dataset_analysis, dataset_biosample, dataset_genomicVariant, dataset_individual, dataset_run, dataset_single, map_individual, individual_analysis, individual_biosample, individual_genomicVariant, individual_run, individual_single, map_run, run_analysis, run_genomicVariant, run_single, map_genomicVariant, genomicVariant_analysis, genomicVariant_biosample, genomicVariant_individual, genomicVariant_run, genomicVariant_single

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

def get_entry_types_map(self):
    map_entry_types={}
    map_entry_types["endpointSets"]={}
    if analyses["granularity"]["boolean"]==True or analyses["granularity"]["count"]==True or analyses["granularity"]["record"]==True:
        analyses_endpoints={}
        analyses_endpoints["endpoints"]={}
        if analyses["singleEntryUrl"]==True:
            map_analysis["singleEntryUrl"]=analysis_single
        if analyses["endpoints"]["genomicVariant"]==True:
            analyses_endpoints["genomicVariant"]=analysis_genomicVariant
            map_analysis["endpoints"]={}
            map_analysis["endpoints"]["genomicVariant"]=analyses_endpoints
        map_entry_types["endpointSets"]["analysis"]=map_analysis
    if biosamples["granularity"]["boolean"]==True or biosamples["granularity"]["count"]==True or biosamples["granularity"]["record"]==True:
        biosamples_endpoints={}
        biosamples_endpoints["endpoints"]={}
        if biosamples["singleEntryUrl"]==True:
            map_biosample["singleEntryUrl"]=biosample_single
        if biosamples["endpoints"]["genomicVariant"]==True:
            biosamples_endpoints["genomicVariant"]=biosample_genomicVariant
            try:
                map_biosample["endpoints"]["genomicVariant"]=biosamples_endpoints
            except Exception:
                map_biosample["endpoints"]={}
                map_biosample["endpoints"]["genomicVariant"]=biosamples_endpoints
        if biosamples["endpoints"]["analysis"]==True:
            biosamples_endpoints["analysis"]=biosample_analysis
            try:
                map_biosample["endpoints"]["analysis"]=biosamples_endpoints
            except Exception:
                map_biosample["endpoints"]={}
                map_biosample["endpoints"]["analysis"]=biosamples_endpoints
        if biosamples["endpoints"]["run"]==True:
            biosamples_endpoints["run"]=biosample_run
            try:
                map_biosample["endpoints"]["run"]=biosamples_endpoints
            except Exception:
                map_biosample["endpoints"]={}
                map_biosample["endpoints"]["run"]=biosamples_endpoints
        map_entry_types["endpointSets"]["biosample"]=map_biosample
    if cohorts["granularity"]["boolean"]==True or cohorts["granularity"]["count"]==True or cohorts["granularity"]["record"]==True:
        cohorts_endpoints={}
        cohorts_endpoints["endpoints"]={}
        if cohorts["singleEntryUrl"]==True:
            map_cohort["singleEntryUrl"]=cohort_single
        if cohorts["endpoints"]["individual"]==True:
            cohorts_endpoints["individual"]=cohort_individual
            try:
                map_cohort["endpoints"]["individual"]=cohorts_endpoints
            except Exception:
                map_cohort["endpoints"]={}
                map_cohort["endpoints"]["individual"]=cohorts_endpoints
        if cohorts["endpoints"]["analysis"]==True:
            cohorts_endpoints["analysis"]=cohort_analysis
            try:
                map_cohort["endpoints"]["analysis"]=cohorts_endpoints
            except Exception:
                map_cohort["endpoints"]={}
                map_cohort["endpoints"]["analysis"]=cohorts_endpoints
        if cohorts["endpoints"]["run"]==True:
            cohorts_endpoints["run"]=cohort_run
            try:
                map_cohort["endpoints"]["run"]=cohorts_endpoints
            except Exception:
                map_cohort["endpoints"]={}
                map_cohort["endpoints"]["run"]=cohorts_endpoints
        map_entry_types["endpointSets"]["cohort"]=map_cohort
    if datasets["granularity"]["boolean"]==True or datasets["granularity"]["count"]==True or datasets["granularity"]["record"]==True:
        datasets_endpoints={}
        datasets_endpoints["endpoints"]={}
        if datasets["singleEntryUrl"]==True:
            map_dataset["singleEntryUrl"]=dataset_single
        if datasets["endpoints"]["individual"]==True:
            datasets_endpoints["individual"]=dataset_individual
            try:
                map_dataset["endpoints"]["individual"]=datasets_endpoints
            except Exception:
                map_dataset["endpoints"]={}
                map_dataset["endpoints"]["individual"]=datasets_endpoints
        if datasets["endpoints"]["analysis"]==True:
            datasets_endpoints["analysis"]=dataset_analysis
            try:
                map_dataset["endpoints"]["analysis"]=datasets_endpoints
            except Exception:
                map_dataset["endpoints"]={}
                map_dataset["endpoints"]["analysis"]=datasets_endpoints
        if datasets["endpoints"]["run"]==True:
            datasets_endpoints["run"]=dataset_run
            try:
                map_dataset["endpoints"]["run"]=datasets_endpoints
            except Exception:
                map_dataset["endpoints"]={}
                map_dataset["endpoints"]["run"]=datasets_endpoints
        if datasets["endpoints"]["biosample"]==True:
            datasets_endpoints["biosample"]=dataset_biosample
            try:
                map_dataset["endpoints"]["biosample"]=datasets_endpoints
            except Exception:
                map_dataset["endpoints"]={}
                map_dataset["endpoints"]["biosample"]=datasets_endpoints
        if datasets["endpoints"]["genomicVariant"]==True:
            datasets_endpoints["genomicVariant"]=dataset_genomicVariant
            try:
                map_dataset["endpoints"]["genomicVariant"]=datasets_endpoints
            except Exception:
                map_dataset["endpoints"]={}
                map_dataset["endpoints"]["genomicVariant"]=datasets_endpoints
        map_entry_types["endpointSets"]["dataset"]=map_dataset
    if g_variants["granularity"]["boolean"]==True or g_variants["granularity"]["count"]==True or g_variants["granularity"]["record"]==True:
        g_variants_endpoints={}
        g_variants_endpoints["endpoints"]={}
        if g_variants["singleEntryUrl"]==True:
            map_genomicVariant["singleEntryUrl"]=genomicVariant_single
        if g_variants["endpoints"]["individual"]==True:
            g_variants_endpoints["individual"]=genomicVariant_individual
            try:
                map_genomicVariant["endpoints"]["individual"]=g_variants_endpoints
            except Exception:
                map_genomicVariant["endpoints"]={}
                map_genomicVariant["endpoints"]["individual"]=g_variants_endpoints
        if g_variants["endpoints"]["analysis"]==True:
            g_variants_endpoints["analysis"]=genomicVariant_analysis
            try:
                map_genomicVariant["endpoints"]["analysis"]=g_variants_endpoints
            except Exception:
                map_genomicVariant["endpoints"]={}
                map_genomicVariant["endpoints"]["analysis"]=g_variants_endpoints
        if g_variants["endpoints"]["run"]==True:
            g_variants_endpoints["run"]=genomicVariant_run
            try:
                map_genomicVariant["endpoints"]["run"]=g_variants_endpoints
            except Exception:
                map_genomicVariant["endpoints"]={}
                map_genomicVariant["endpoints"]["run"]=g_variants_endpoints
        if g_variants["endpoints"]["biosample"]==True:
            g_variants_endpoints["biosample"]=genomicVariant_biosample
            try:
                map_genomicVariant["endpoints"]["biosample"]=g_variants_endpoints
            except Exception:
                map_genomicVariant["endpoints"]={}
                map_genomicVariant["endpoints"]["biosample"]=g_variants_endpoints
        map_entry_types["endpointSets"]["genomicVariant"]=map_genomicVariant
    if individuals["granularity"]["boolean"]==True or individuals["granularity"]["count"]==True or individuals["granularity"]["record"]==True:
        individuals_endpoints={}
        individuals_endpoints["endpoints"]={}
        if individuals["singleEntryUrl"]==True:
            map_individual["singleEntryUrl"]=individual_single
        if individuals["endpoints"]["genomicVariant"]==True:
            individuals_endpoints["genomicVariant"]=individual_genomicVariant
            try:
                map_individual["endpoints"]["genomicVariant"]=individuals_endpoints
            except Exception:
                map_individual["endpoints"]={}
                map_individual["endpoints"]["genomicVariant"]=individuals_endpoints
        if individuals["endpoints"]["analysis"]==True:
            individuals_endpoints["analysis"]=individual_analysis
            try:
                map_individual["endpoints"]["analysis"]=individuals_endpoints
            except Exception:
                map_individual["endpoints"]={}
                map_individual["endpoints"]["analysis"]=individuals_endpoints
        if individuals["endpoints"]["run"]==True:
            individuals_endpoints["run"]=individual_run
            try:
                map_individual["endpoints"]["run"]=individuals_endpoints
            except Exception:
                map_individual["endpoints"]={}
                map_individual["endpoints"]["run"]=individuals_endpoints
        if individuals["endpoints"]["biosample"]==True:
            individuals_endpoints["biosample"]=individual_biosample
            try:
                map_individual["endpoints"]["biosample"]=individuals_endpoints
            except Exception:
                map_individual["endpoints"]={}
                map_individual["endpoints"]["biosample"]=individuals_endpoints
        map_entry_types["endpointSets"]["individual"]=map_individual
    if runs["granularity"]["boolean"]==True or runs["granularity"]["count"]==True or runs["granularity"]["record"]==True:
        runs_endpoints={}
        runs_endpoints["endpoints"]={}
        if runs["singleEntryUrl"]==True:
            map_run["singleEntryUrl"]=run_single
        if runs["endpoints"]["genomicVariant"]==True:
            runs_endpoints["genomicVariant"]=run_genomicVariant
            try:
                map_run["endpoints"]["genomicVariant"]=runs_endpoints
            except Exception:
                map_run["endpoints"]={}
                map_run["endpoints"]["genomicVariant"]=runs_endpoints
        if runs["endpoints"]["analysis"]==True:
            runs_endpoints["analysis"]=run_analysis
            try:
                map_run["endpoints"]["analysis"]=runs_endpoints
            except Exception:
                map_run["endpoints"]={}
                map_run["endpoints"]["analysis"]=runs_endpoints
        map_entry_types["endpointSets"]["run"]=map_run

    return map_entry_types