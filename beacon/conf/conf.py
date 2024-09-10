import logging
import yaml

with open("beacon/conf/api_version.yml") as api_version_file:
    api_version_yaml = yaml.safe_load(api_version_file)

level=logging.DEBUG
api_version='2.0.0'
default_beacon_granularity='record'
beacon_id = 'org.ega-archive.beacon-ri-demo'  # ID of the Beacon
beacon_name = 'Beacon Reference Implementation demo'  # Name of the Beacon service
api_version = 'v2.0.0' # Version of the Beacon implementation
uri = 'https://beacon-ri-demo.ega-archive.org/api/'
environment = 'test'
description = r"This Beacon is based on synthetic data hosted at the <a href='https://ega-archive.org/datasets/EGAD00001003338'>EGA</a>. The dataset contains 2504 samples including genetic data based on 1K Genomes data, and 76 individual attributes and phenotypic data derived from UKBiobank."
version = api_version_yaml['api_version']
welcome_url = 'https://beacon.ega-archive.org/'
alternative_url = 'https://beacon.ega-archive.org/api'
create_datetime = '2021-11-29T12:00:00.000000'
update_datetime = ''
default_beacon_granularity = "record"
security_levels = ['PUBLIC', 'REGISTERED', 'CONTROLLED']

# Organization info
org_id = 'EGA'  # Id of the organization
org_name = 'European Genome-Phenome Archive (EGA)'  # Full name
org_description = ('The European Genome-phenome Archive (EGA) '
                   'is a service for permanent archiving and sharing '
                   'of all types of personally identifiable genetic '
                   'and phenotypic data resulting from biomedical research projects.')
org_adress = ('C/ Dr. Aiguader, 88'
              'PRBB Building'
              '08003 Barcelona, Spain')
org_welcome_url = 'https://ega-archive.org/'
org_contact_url = 'mailto:beacon.ega@crg.eu'
org_logo_url = 'https://legacy.ega-archive.org/images/logo.png'
org_info = ''