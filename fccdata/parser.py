#!/home/bin/python
# -*- coding: utf-8
"""
    Necessary import order:
        EN, AM (HD?)
"""


def cleanup(value):
    value = str(value)
    value = value.replace("\xBD", " 1/2")  # ½, 215830
    value = value.replace("\xF1", "n")  # ñ, 620769
    value = value.replace("\xC9", "E")  # É, 645181
    value = value.replace("\xD1", "N")  # Ñ, 931395
    value = value.replace("\xE1", "a")  # a, 1077346
    value = value.replace("\xE6", "ae")  # æ, 1579078
    value = value.replace("\xF3", "o")  # ó, 2388090
    value = value.replace("\xE9", "e")  # é, 2716958
    value = value.replace("\xF2", "o")  # ò, 3052388
    value = value.replace("\xA0", " ")  #  , 495563
    value = value.replace("\xF6", "ö")  # ö, 614011
    value = value.replace("\xD2", "Ò")  # Ò, 2942093
    value = value.replace("\xD8", "Ø")  # Ø, 2767585
    value = value.replace("\xDC", "Ü")  # Ü, 1949538
    return value


class AM(object):
    definition = """
    AM|2840548|||KC0YLK|G|D|10|||||||||T|
    record_type               char(2)              not null,
    unique_system_identifier  numeric(9,0)         not null,
    uls_file_num              char(14)             null,
    ebf_number                varchar(30)          null,
    callsign                  char(10)             null,
    operator_class            char(1)              null,
    group_code                char(1)              null,
    region_code               tinyint              null,
    trustee_callsign          char(10)             null,
    trustee_indicator         char(1)              null,
    physician_certification   char(1)              null,
    ve_signature              char(1)              null,
    systematic_callsign_change char(1)             null,
    vanity_callsign_change    char(1)              null,
    vanity_relationship       char(12)             null,
    previous_callsign         char(10)             null,
    previous_operator_class   char(1)              null,
    trustee_name              varchar(50)          null
    """

    def __init__(self, input):
        data = input.split('|')
        self.record_type = 'AM'
        self.unique_system_identifier = data[1]
        self.uls_file_num = data[2]
        self.ebf_number = data[3]
        self.callsign = data[4]
        self.operator_class = data[5]
        self.group_code = data[6]
        if data[7]:
            self.region_code = data[7]
        else:
            self.region_code = None
        self.trustee_callsign = data[8]
        self.trustee_indicator = data[9]
        self.physician_certification = data[10]
        self.ve_signature = data[11]
        self.systematic_callsign_change = data[12]
        self.vanity_callsign_change = data[13]
        self.vanity_relationship = data[14]
        self.previous_callsign = data[15]
        self.previous_operator_class = data[16]
        self.trustee_name = data[17]

    def get_object(self):
        definition = """
            record_type = models.CharField(max_length=2, blank=True, null=True)
            unique_system_identifier = models.OneToOneField(en, db_column='unique_system_identifier', blank=True, null=True, primary_key=True)
            uls_file_number = models.CharField(max_length=14, blank=True, null=True)
            ebf_number = models.CharField(max_length=30, blank=True, null=True)
            call_sign = models.CharField(max_length=10, blank=True, null=True)
            operator_class = models.CharField(max_length=1, blank=True, null=True)
            group_code = models.CharField(max_length=1, blank=True, null=True)
            region_code = models.IntegerField(blank=True, null=True)
            trustee_call_sign = models.CharField(max_length=10, blank=True, null=True)
            trustee_indicator = models.CharField(max_length=1, blank=True, null=True)
            physician_certification = models.CharField(max_length=1, blank=True, null=True)
            ve_signature = models.CharField(max_length=1, blank=True, null=True)
            systematic_call_sign_change = models.CharField(max_length=1, blank=True, null=True)
            vanity_call_sign_change = models.CharField(max_length=1, blank=True, null=True)
            vanity_relationship = models.CharField(max_length=12, blank=True, null=True)
            previous_call_sign = models.CharField(max_length=10, blank=True, null=True)
            previous_operator_class = models.CharField(max_length=1, blank=True, null=True)
            trustee_name = models.CharField(max_length=50, blank=True, null=True)
        """

        from fccdata.models import am, en
        en_obj = en.objects.get(unique_system_identifier=self.unique_system_identifier)
        try:
            obj = am.objects.get(unique_system_identifier=en_obj)
        except am.DoesNotExist:
            obj = am(record_type='AM', unique_system_identifier=en_obj)
        # now update the rest
        obj.uls_file_number = self.uls_file_num
        obj.ebf_number = self.ebf_number
        obj.call_sign = self.callsign
        obj.operator_class = self.operator_class
        obj.group_code = self.group_code
        obj.region_code = self.region_code
        obj.trustee_call_sign = self.trustee_callsign
        obj.trustee_indicator = self.trustee_indicator
        obj.physician_certification = self.physician_certification
        obj.ve_signature = self.ve_signature
        obj.systematic_call_sign_change = self.systematic_callsign_change
        obj.vanity_call_sign_change = self.vanity_callsign_change
        obj.vanity_relationship = self.vanity_relationship
        obj.previous_call_sign = self.previous_callsign
        obj.previous_operator_class = self.previous_operator_class
        obj.trustee_name = self.trustee_name

        return obj


class EN(object):
    definition = """
        record_type               char(2)              not null,
        unique_system_identifier  numeric(9,0)         not null,
        uls_file_number           char(14)             null,
        ebf_number                varchar(30)          null,
        call_sign                 char(10)             null,
        entity_type               char(2)              null,
        licensee_id               char(9)              null,
        entity_name               varchar(200)         null,
        first_name                varchar(20)          null,
        mi                        char(1)              null,
        last_name                 varchar(20)          null,
        suffix                    char(3)              null,
        phone                     char(10)             null,
        fax                       char(10)             null,
        email                     varchar(50)          null,
        street_address            varchar(60)          null,
        city                      varchar(20)          null,
        state                     char(2)              null,
        zip_code                  char(9)              null,
        po_box                    varchar(20)          null,
        attention_line            varchar(35)          null,
        sgin                      char(3)              null,
        frn                       char(10)             null,
        applicant_type_code       char(1)              null,
        applicant_type_other      char(40)             null,
        status_code               char(1)            null,
        status_date     datetime         null
    """

    def __init__(self, input):
        import datetime, time

        data = input.split('|')
        self.record_type = 'EN'
        self.unique_system_identifier = data[1]
        self.uls_file_number = data[2]
        self.ebf_number = data[3]
        self.call_sign = data[4]
        self.entity_type = data[5]
        self.licensee_id = data[6]
        self.entity_name = cleanup(data[7])
        self.first_name = cleanup(data[8])
        self.mi = data[9]
        self.last_name = cleanup(data[10])
        self.suffix = data[11]
        self.phone = data[12]
        self.fax = data[13]
        self.email = data[14]
        self.street_address = cleanup(data[15])
        self.city = cleanup(data[16])
        self.state = data[17]
        self.zip_code = data[18]
        self.po_box = data[19]
        self.attention_line = cleanup(data[20])
        self.sgin = data[21]
        self.frn = data[22]
        self.applicant_type_code = data[23]
        self.applicant_type_other = data[24]
        self.status_code = data[25]
        if data[26]:
            self.status_date = datetime.datetime(*time.strptime(u'%s' % data[26], "%m/%d/%Y")[0:5])
        else:
            self.status_date = None

    def get_object(self):
        definition = """
            record_type = models.CharField(max_length=2, blank=True, null=True)
            unique_system_identifier = models.IntegerField(blank=True, null=True, primary_key=True)
            uls_file_number = models.CharField(max_length=14, blank=True, null=True)
            ebf_number = models.CharField(max_length=30, blank=True, null=True)
            call_sign = models.CharField(max_length=10, blank=True, null=True)
            entity_type = models.CharField(max_length=2, blank=True, null=True)
            licensee_id = models.CharField(max_length=9, blank=True, null=True)
            entity_name = models.CharField(max_length=200, blank=True, null=True)
            first_name = models.CharField(max_length=20, blank=True, null=True)
            mi = models.CharField(max_length=1, blank=True, null=True)
            last_name = models.CharField(max_length=20, blank=True, null=True)
            suffix = models.CharField(max_length=3, blank=True, null=True)
            phone = models.CharField(max_length=10, blank=True, null=True)
            fax = models.CharField(max_length=10, blank=True, null=True)
            email = models.CharField(max_length=50, blank=True, null=True)
            street_address = models.CharField(max_length=60, blank=True, null=True)
            city = models.CharField(max_length=20, blank=True, null=True)
            state = models.CharField(max_length=2, blank=True, null=True)
            zip_code = models.CharField(max_length=9, blank=True, null=True)
            po_box = models.CharField(max_length=20, blank=True, null=True)
            attention_line = models.CharField(max_length=35, blank=True, null=True)
            sgin = models.CharField(max_length=3, blank=True, null=True)
            frn = models.CharField('fcc registration number', max_length=10, blank=True, null=True)
            applicant_type_code = models.CharField(max_length=1, blank=True, null=True)
            applicant_type_code_other = models.CharField(max_length=40, blank=True, null=True)
            status_code = models.CharField(max_length=1, blank=True, null=True)
            status_date = models.DateField(blank=True, null=True)
        """
        from fccdata.models import en
        try:
            obj = en.objects.get(unique_system_identifier=self.unique_system_identifier)
        except en.DoesNotExist:
            obj = en(record_type='EN', unique_system_identifier=self.unique_system_identifier)
        # now update the rest
        obj.uls_file_number = self.uls_file_number,
        obj.ebf_number = self.ebf_number
        obj.call_sign = self.call_sign
        obj.entity_type = self.entity_type
        obj.licensee_id = self.licensee_id
        obj.entity_name = self.entity_name
        obj.first_name = self.first_name
        obj.mi = self.mi
        obj.last_name = self.last_name
        obj.suffix = self.suffix
        obj.phone = self.phone
        obj.fax = self.fax
        obj.email = self.email
        obj.street_address = self.street_address
        obj.city = self.city
        obj.state = self.state
        obj.zip_code = self.zip_code
        obj.po_box = self.po_box
        obj.attention_line = self.attention_line
        obj.sgin = self.sgin
        obj.frn = self.frn
        obj.applicant_type_code = self.applicant_type_code
        obj.applicant_type_code_other = self.applicant_type_other
        obj.status_code = self.status_code
        obj.status_date = self.status_date

        return obj


class HD(object):
    definition = """
        record_type               char(2)              not null,
        unique_system_identifier  numeric(9,0)         not null,
        uls_file_number           char(14)             null,
        ebf_number                varchar(30)          null,
        call_sign                 char(10)             null,
        license_status            char(1)              null,
        radio_service_code        char(2)              null,
        grant_date                char(10)             null,
        expired_date              char(10)             null,
        cancellation_date         char(10)             null,
        eligibility_rule_num      char(10)             null,
        applicant_type_code_reserved       char(1)              null,
        alien                     char(1)              null,
        alien_government          char(1)              null,
        alien_corporation         char(1)              null,
        alien_officer             char(1)              null,
        alien_control             char(1)              null,
        revoked                   char(1)              null,
        convicted                 char(1)              null,
        adjudged                  char(1)              null,
        involved_reserved       char(1)              null,
        common_carrier            char(1)              null,
        non_common_carrier        char(1)              null,
        private_comm              char(1)              null,
        fixed                     char(1)              null,
        mobile                    char(1)              null,
        radiolocation             char(1)              null,
        satellite                 char(1)              null,
        developmental_or_sta      char(1)              null,
        interconnected_service    char(1)              null,
        certifier_first_name      varchar(20)          null,
        certifier_mi              char(1)              null,
        certifier_last_name       varchar(20)          null,
        certifier_suffix          char(3)              null,
        certifier_title           char(40)             null,
        gender                    char(1)              null,
        african_american          char(1)              null,
        native_american           char(1)              null,
        hawaiian                  char(1)              null,
        asian                     char(1)              null,
        white                     char(1)              null,
        ethnicity                 char(1)              null,
        effective_date            char(10)             null,
        last_action_date          char(10)             null,
        auction_id                int                  null,
        reg_stat_broad_serv       char(1)              null,
        band_manager              char(1)              null,
        type_serv_broad_serv      char(1)              null,
        alien_ruling              char(1)              null,
        licensee_name_change    char(1)          null
    """

    def __init__(self, input):
        import datetime, time
        data = input.split('|')
        self.record_type = 'HD'
        self.unique_system_identifier = data[1]
        self.uls_file_number = data[2]
        self.ebf_number = data[3]
        self.call_sign = data[4]
        self.license_status = data[5]
        self.radio_service_code = data[6]
        if data[7]:
            self.grant_date = datetime.datetime(*time.strptime(u'%s' % data[7], "%m/%d/%Y")[0:5])
        else:
            self.grant_date = None
        if data[8]:
            self.expired_date = datetime.datetime(*time.strptime(u'%s' % data[8], "%m/%d/%Y")[0:5])
        else:
            self.expired_date = None
        if data[9]:
            self.cancellation_date = datetime.datetime(*time.strptime(u'%s' % data[9], "%m/%d/%Y")[0:5])
        else:
            self.cancellation_date = None
        self.eligibility_rule_number = data[10]
        self.reserved = data[11]
        self.alien = data[12]
        self.alien_government = data[13]
        self.alien_corporation = data[14]
        self.alien_officer = data[15]
        self.alien_control = data[16]
        self.revoked = data[17]
        self.convicted = data[18]
        self.adjudged = data[19]
        self.reserved = data[20]
        self.common_carrier = data[21]
        self.non_common_carrier = data[22]
        self.private_comm = data[23]
        self.fixed = data[24]
        self.mobile = data[25]
        self.radiolocation = data[26]
        self.satellite = data[27]
        self.developmental_sta_demonstration = data[28]
        self.interconnected_service = data[29]
        self.certifier_first_name = cleanup(data[30])
        self.certifier_mi = data[31]
        self.certifier_last_name = cleanup(data[32])
        self.certifier_suffix = data[33]
        self.certifier_title = cleanup(data[34])
        self.female = data[35]
        self.black_african_american = data[36]
        self.native_american = data[37]
        self.hawaiian = data[38]
        self.asian = data[39]
        self.white = data[40]
        self.hispanic = data[41]
        if data[42]:
            self.effective_date = datetime.datetime(*time.strptime(u'%s' % data[42], "%m/%d/%Y")[0:5])
        else:
            self.effective_date = None
        if data[43]:
            self.last_action_date = datetime.datetime(*time.strptime(u'%s' % data[43], "%m/%d/%Y")[0:5])
        else:
            self.last_action_date = None
        if data[44]:
            self.auction_id = data[44]
        else:
            self.auction_id = None
        self.broadcast_services_regulatory_status = data[45]
        self.band_manager_regulatory_status = data[46]
        self.broadcast_services_type_of_radio_service = data[47]
        self.alien_ruling = data[48]
        self.licensee_name_change = cleanup(data[49])

    def get_object(self):
        definition = """
            record_type = models.CharField(max_length=2, blank=True, null=True)
            unique_system_identifier = models.OneToOneField(en, db_column='unique_system_identifier', blank=True, null=True, primary_key=True)
            uls_file_number = models.CharField(max_length=14, blank=True, null=True)
            ebf_number = models.CharField(max_length=30, blank=True, null=True)
            call_sign = models.CharField(max_length=10, blank=True, null=True)
            license_status = models.CharField(max_length=1, blank=True, null=True)
            radio_service_code = models.CharField(max_length=2, blank=True, null=True)
            grant_date = models.DateField(blank=True, null=True)
            expired_date = models.DateField(blank=True, null=True)
            cancellation_date = models.DateField(blank=True, null=True)
            eligibility_rule_number = models.CharField(max_length=10, blank=True, null=True)
            reserved = models.CharField(max_length=1, blank=True, null=True)
            alien = models.CharField(max_length=1, blank=True, null=True)
            alien_government = models.CharField(max_length=1, blank=True, null=True)
            alien_corporation = models.CharField(max_length=1, blank=True, null=True)
            alien_officer = models.CharField(max_length=1, blank=True, null=True)
            alien_control = models.CharField(max_length=1, blank=True, null=True)
            revoked = models.CharField(max_length=1, blank=True, null=True)
            convicted = models.CharField(max_length=1, blank=True, null=True)
            adjudged = models.CharField(max_length=1, blank=True, null=True)
            reserved = models.CharField(max_length=1, blank=True, null=True)
            common_carrier = models.CharField(max_length=1, blank=True, null=True)
            non_common_carrier = models.CharField(max_length=1, blank=True, null=True)
            private_comm = models.CharField(max_length=1, blank=True, null=True)
            fixed = models.CharField(max_length=1, blank=True, null=True)
            mobile = models.CharField(max_length=1, blank=True, null=True)
            radiolocation = models.CharField(max_length=1, blank=True, null=True)
            satellite = models.CharField(max_length=1, blank=True, null=True)
            developmental_sta_demonstration = models.CharField(max_length=1, blank=True, null=True)
            interconnected_service = models.CharField(max_length=1, blank=True, null=True)
            certifier_first_name = models.CharField(max_length=20, blank=True, null=True)
            certifier_mi = models.CharField(max_length=1, blank=True, null=True)
            certifier_last_name = models.CharField(max_length=20, blank=True, null=True)
            certifier_suffix = models.CharField(max_length=3, blank=True, null=True)
            certifier_title = models.CharField(max_length=40, blank=True, null=True)
            female = models.CharField(max_length=1, blank=True, null=True)
            black_african_american = models.CharField(max_length=1, blank=True, null=True)
            native_american = models.CharField(max_length=1, blank=True, null=True)
            hawaiian = models.CharField(max_length=1, blank=True, null=True)
            asian = models.CharField(max_length=1, blank=True, null=True)
            white = models.CharField(max_length=1, blank=True, null=True)
            hispanic = models.CharField(max_length=1, blank=True, null=True)
            effective_date = models.DateField(blank=True, null=True)
            last_action_date = models.DateField(blank=True, null=True)
            auction_id = models.IntegerField(blank=True, null=True)
            broadcast_services_regulatory_status = models.CharField(max_length=1, blank=True, null=True)
            band_manager_regulatory_status = models.CharField(max_length=1, blank=True, null=True)
            broadcast_services_type_of_radio_service = models.CharField(max_length=1, blank=True, null=True)
            alien_ruling = models.CharField(max_length=1, blank=True, null=True)
            licensee_name_change = models.CharField(max_length=1, blank=True, null=True)
        """
        from fccdata.models import en, hd
        en_obj = en.objects.get(unique_system_identifier=self.unique_system_identifier)

        try:
            obj = hd.objects.get(unique_system_identifier=en_obj)
        except hd.DoesNotExist:
            obj = hd(record_type='HD', unique_system_identifier=en_obj)
        # now update the rest
        obj.uls_file_number = self.uls_file_number
        obj.ebf_number = self.ebf_number
        obj.call_sign = self.call_sign
        obj.license_status = self.license_status
        obj.radio_service_code = self.radio_service_code
        obj.grant_date = self.grant_date
        obj.expired_date = self.expired_date
        obj.cancellation_date = self.cancellation_date
        obj.eligibility_rule_number = self.eligibility_rule_number
        obj.alien = self.alien
        obj.alien_government = self.alien_government
        obj.alien_corporation = self.alien_corporation
        obj.alien_officer = self.alien_officer
        obj.alien_control = self.alien_control
        obj.revoked = self.revoked
        obj.convicted = self.convicted
        obj.adjudged = self.adjudged
        obj.reserved = self.reserved
        obj.common_carrier = self.common_carrier
        obj.non_common_carrier = self.non_common_carrier
        obj.private_comm = self.private_comm
        obj.fixed = self.fixed
        obj.mobile = self.mobile
        obj.radiolocation = self.radiolocation
        obj.satellite = self.satellite
        obj.developmental_sta_demonstration = self.developmental_sta_demonstration
        obj.interconnected_service = self.interconnected_service
        obj.certifier_first_name = self.certifier_first_name
        obj.certifier_mi = self.certifier_mi
        obj.certifier_last_name = self.certifier_last_name
        obj.certifier_suffix = self.certifier_suffix
        obj.certifier_title = self.certifier_title
        obj.female = self.female
        obj.black_african_american = self.black_african_american
        obj.native_american = self.native_american
        obj.hawaiian = self.hawaiian
        obj.asian = self.asian
        obj.white = self.white
        obj.hispanic = self.hispanic
        obj.effective_date = self.effective_date
        obj.last_action_date = self.last_action_date
        obj.auction_id = self.auction_id
        obj.broadcast_services_regulatory_status = self.broadcast_services_regulatory_status
        obj.band_manager_regulatory_status = self.band_manager_regulatory_status
        obj.broadcast_services_type_of_radio_service = self.broadcast_services_type_of_radio_service
        obj.alien_ruling = self.alien_ruling
        obj.licensee_name_change = self.licensee_name_change

        return obj
