import datetime
from django.test import TestCase
from fccdata.models import am, en, hd
from fccdata.parser import AM, EN, HD

class ENParserTest(TestCase):
    """
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
        status_code               char(1)		     null,
        status_date		datetime	     null
    """

    def test_kc0ylk(self):
        en_obj = EN('EN|2840548|||KC0YLK|L|L00615690|Fast, Adam G|Adam|G|Fast|||||1501 George Williams Way Apt. F9|Lawrence|KS|66047|||000|0008178568|I|||')
        self.assertEqual(en_obj.unique_system_identifier, '2840548')
        self.assertEqual(en_obj.uls_file_number, '')
        self.assertEqual(en_obj.call_sign, 'KC0YLK')
        self.assertEqual(en_obj.entity_type, 'L')
        self.assertEqual(en_obj.licensee_id, 'L00615690')
        self.assertEqual(en_obj.entity_name, 'Fast, Adam G')
        self.assertEqual(en_obj.first_name, 'Adam')
        self.assertEqual(en_obj.mi, 'G')
        self.assertEqual(en_obj.last_name, 'Fast')
        self.assertEqual(en_obj.zip_code, '66047')
        self.assertEqual(en_obj.frn, '0008178568')
        self.assertEqual(en_obj.status_code, '')
        self.assertEqual(en_obj.status_date, None)

    def test_kg0w_cancelled(self):
        en_obj = EN('EN|599000|||KG0W|L|L00268694|ETIENNE, ANTHONY J|ANTHONY|J|ETIENNE||||||OSCEOLA|NE|686510316|316||000|0003882503|I|||')
        self.assertEqual(en_obj.unique_system_identifier, '599000')
        self.assertEqual(en_obj.uls_file_number, '')
        self.assertEqual(en_obj.call_sign, 'KG0W')
        self.assertEqual(en_obj.entity_type, 'L')
        self.assertEqual(en_obj.licensee_id, 'L00268694')
        self.assertEqual(en_obj.entity_name, 'ETIENNE, ANTHONY J')
        self.assertEqual(en_obj.first_name, 'ANTHONY')
        self.assertEqual(en_obj.mi, 'J')
        self.assertEqual(en_obj.last_name, 'ETIENNE')
        self.assertEqual(en_obj.zip_code, '686510316')
        self.assertEqual(en_obj.frn, '0003882503')
        self.assertEqual(en_obj.status_code, '')
        self.assertEqual(en_obj.status_date, None)

    def test_kg0w_active(self):
        en_obj = EN('EN|2867281|||KG0W|L|L00170412|KASSAWARA, MATTHEW S|MATTHEW|S|KASSAWARA|||||1681 W Canal Cir Unit 121|Littleton|CO|80120|||000|0002451524|I|||')
        self.assertEqual(en_obj.unique_system_identifier, '2867281')
        self.assertEqual(en_obj.uls_file_number, '')
        self.assertEqual(en_obj.call_sign, 'KG0W')
        self.assertEqual(en_obj.entity_type, 'L')
        self.assertEqual(en_obj.licensee_id, 'L00170412')
        self.assertEqual(en_obj.entity_name, 'KASSAWARA, MATTHEW S')
        self.assertEqual(en_obj.first_name, 'MATTHEW')
        self.assertEqual(en_obj.mi, 'S')
        self.assertEqual(en_obj.last_name, 'KASSAWARA')
        self.assertEqual(en_obj.zip_code, '80120')
        self.assertEqual(en_obj.frn, '0002451524')
        self.assertEqual(en_obj.status_code, '')
        self.assertEqual(en_obj.status_date, None)

class AMParserTest(TestCase):
    """
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

    def test_kc0ylk(self):
        # get set up
        en_parse = EN('EN|2840548|||KC0YLK|L|L00615690|Fast, Adam G|Adam|G|Fast|||||1501 George Williams Way Apt. F9|Lawrence|KS|66047|||000|0008178568|I|||')
        en_parse.get_object().save()

        am_obj = AM('AM|2840548|||KC0YLK|E|D|10|||||||||G|')
        am_obj.get_object().save()
        self.assertEqual(am_obj.unique_system_identifier, str(en_parse.get_object().unique_system_identifier))
        self.assertEqual(am_obj.callsign, 'KC0YLK')
        self.assertEqual(am_obj.operator_class, 'E')
        self.assertEqual(am_obj.group_code, 'D')
        self.assertEqual(am_obj.region_code, '10')
        self.assertEqual(am_obj.previous_callsign, '')
        self.assertEqual(am_obj.previous_operator_class, 'G')
        self.assertEqual(am_obj.trustee_name, '')

        en_obj = en.objects.get(unique_system_identifier='2840548')
        am = am_obj.get_object()
        self.assertEqual(am.record_type, 'AM')
        self.assertEqual(am.unique_system_identifier, en_parse.get_object())
        self.assertEqual(am.call_sign, 'KC0YLK')
        self.assertEqual(am.operator_class, 'E')
        self.assertEqual(am.group_code, 'D')
        self.assertEqual(am.region_code, '10')
        self.assertEqual(am.previous_operator_class, 'G')

    def test_kg0w_cancelled(self):
        # get set up
        en_parse = EN('EN|599000|||KG0W|L|L00268694|ETIENNE, ANTHONY J|ANTHONY|J|ETIENNE||||||OSCEOLA|NE|686510316|316||000|0003882503|I|||')
        en_parse.get_object().save()

        am_obj = AM('AM|599000|||KG0W|E|A|10||||||||||')
        am_obj.get_object().save()
        self.assertEqual(am_obj.unique_system_identifier, str(en_parse.get_object().unique_system_identifier))
        self.assertEqual(am_obj.callsign, 'KG0W')
        self.assertEqual(am_obj.operator_class, 'E')
        self.assertEqual(am_obj.group_code, 'A')
        self.assertEqual(am_obj.region_code, '10')
        self.assertEqual(am_obj.previous_callsign, '')
        self.assertEqual(am_obj.previous_operator_class, '')
        self.assertEqual(am_obj.trustee_name, '')

        en_obj = en.objects.get(unique_system_identifier=str(en_parse.get_object().unique_system_identifier))
        am = am_obj.get_object()
        self.assertEqual(am.record_type, 'AM')
        self.assertEqual(am.unique_system_identifier, en_parse.get_object()),
        self.assertEqual(am.call_sign, 'KG0W')
        self.assertEqual(am.operator_class, 'E')
        self.assertEqual(am.group_code, 'A')
        self.assertEqual(am.region_code, '10')
        self.assertEqual(am.previous_operator_class, '')

    def test_kg0w_active(self):
        # get set up
        en_parse = EN('EN|2867281|||KG0W|L|L00170412|KASSAWARA, MATTHEW S|MATTHEW|S|KASSAWARA|||||1681 W Canal Cir Unit 121|Littleton|CO|80120|||000|0002451524|I|||')
        en_parse.get_object().save()

        am_obj = AM('AM|2867281|||KG0W|E|A|10||||||E||KG4FEQ|G|')
        am_obj.get_object().save()
        self.assertEqual(am_obj.unique_system_identifier, str(en_parse.get_object().unique_system_identifier))
        self.assertEqual(am_obj.callsign, 'KG0W')
        self.assertEqual(am_obj.operator_class, 'E')
        self.assertEqual(am_obj.group_code, 'A')
        self.assertEqual(am_obj.region_code, '10')
        self.assertEqual(am_obj.previous_callsign, 'KG4FEQ')
        self.assertEqual(am_obj.previous_operator_class, 'G')
        self.assertEqual(am_obj.trustee_name, '')

        en_obj = en.objects.get(unique_system_identifier='2867281')
        am = am_obj.get_object()
        self.assertEqual(am.record_type, 'AM')
        self.assertEqual(am.unique_system_identifier, en_parse.get_object())
        self.assertEqual(am.call_sign, 'KG0W')
        self.assertEqual(am.operator_class, 'E')
        self.assertEqual(am.group_code, 'A')
        self.assertEqual(am.region_code, '10')
        self.assertEqual(am.previous_operator_class, 'G')


class HDParserTest(TestCase):
    """
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
        involved_reserved      	char(1)              null,
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
        licensee_name_change	char(1)		     null
    """

    def test_kc0ylk(self):
        # get set up
        en_parse = EN('EN|2840548|||KC0YLK|L|L00615690|Fast, Adam G|Adam|G|Fast|||||1501 George Williams Way Apt. F9|Lawrence|KS|66047|||000|0008178568|I|||')
        en_parse.get_object().save()

        hd_obj = HD('HD|2840548|0004374840||KC0YLK|A|HA|08/31/2006|08/31/2016||||||||||||||||||||N||Adam|G|Fast||||||||||09/02/2010|09/02/2010||||||')
        hd_obj.get_object().save()
        self.assertEqual(hd_obj.unique_system_identifier, str(en_parse.get_object().unique_system_identifier))
        self.assertEqual(hd_obj.uls_file_number, '0004374840')
        self.assertEqual(hd_obj.call_sign, 'KC0YLK')
        self.assertEqual(hd_obj.license_status, 'A')
        self.assertEqual(hd_obj.radio_service_code, 'HA')
        self.assertEqual(hd_obj.grant_date, datetime.datetime(year=2006, month=8, day=31))
        self.assertEqual(hd_obj.expired_date, datetime.datetime(year=2016, month=8, day=31))
        self.assertEqual(hd_obj.cancellation_date, None)
        self.assertEqual(hd_obj.effective_date, datetime.datetime(year=2010, month=9, day=2))
        self.assertEqual(hd_obj.last_action_date, datetime.datetime(year=2010, month=9, day=2))

        en_obj = en.objects.get(unique_system_identifier='2840548')
        hd = hd_obj.get_object()
        self.assertEqual(hd.record_type, 'HD')
        self.assertEqual(hd.unique_system_identifier, en_obj)
        self.assertEqual(hd.uls_file_number, '0004374840')
        self.assertEqual(hd.call_sign, 'KC0YLK')
        self.assertEqual(hd.license_status, 'A')
        self.assertEqual(hd.radio_service_code, 'HA')
        self.assertEqual(hd.grant_date, datetime.datetime(year=2006, month=8, day=31))
        self.assertEqual(hd.expired_date, datetime.datetime(year=2016, month=8, day=31))
        self.assertEqual(hd.developmental_sta_demonstration, 'N')
        self.assertEqual(hd.certifier_first_name, 'Adam')
        self.assertEqual(hd.certifier_mi, 'G')
        self.assertEqual(hd.certifier_last_name, 'Fast')
        self.assertEqual(hd.effective_date, datetime.datetime(year=2010, month=9, day=2))
        self.assertEqual(hd.last_action_date, datetime.datetime(year=2010, month=9, day=2))

    def test_kg0w_cancelled(self):
        en_parse = EN('EN|599000|||KG0W|L|L00268694|ETIENNE, ANTHONY J|ANTHONY|J|ETIENNE||||||OSCEOLA|NE|686510316|316||000|0003882503|I|||')
        en_parse.get_object().save()

        hd_obj = HD('HD|599000|9905170145||KG0W|C|HA|05/18/1999|04/30/2007|04/21/2003|||||||||||||||||||N||||||||||||||05/18/1999|12/09/2003||||||')
        self.assertEqual(hd_obj.unique_system_identifier, str(en_parse.get_object().unique_system_identifier))
        self.assertEqual(hd_obj.uls_file_number, '9905170145')
        self.assertEqual(hd_obj.call_sign, 'KG0W')
        self.assertEqual(hd_obj.license_status, 'C')
        self.assertEqual(hd_obj.radio_service_code, 'HA')
        self.assertEqual(hd_obj.grant_date, datetime.datetime(year=1999, month=5, day=18))
        self.assertEqual(hd_obj.expired_date, datetime.datetime(year=2007, month=4, day=30))
        self.assertEqual(hd_obj.cancellation_date, datetime.datetime(year=2003, month=4, day=21))
        self.assertEqual(hd_obj.effective_date, datetime.datetime(year=1999, month=5, day=18))
        self.assertEqual(hd_obj.last_action_date, datetime.datetime(year=2003, month=12, day=9))

        en_obj = en.objects.get(unique_system_identifier='599000')
        hd = hd_obj.get_object()
        self.assertEqual(hd.record_type, 'HD')
        self.assertEqual(hd.unique_system_identifier, en_obj)
        self.assertEqual(hd.uls_file_number, '9905170145')
        self.assertEqual(hd.call_sign, 'KG0W')
        self.assertEqual(hd.license_status, 'C')
        self.assertEqual(hd.radio_service_code, 'HA')
        self.assertEqual(hd.grant_date, datetime.datetime(year=1999, month=5, day=18))
        self.assertEqual(hd.expired_date, datetime.datetime(year=2007, month=4, day=30))
        self.assertEqual(hd.developmental_sta_demonstration, 'N')
        self.assertEqual(hd.certifier_first_name, '')
        self.assertEqual(hd.certifier_mi, '')
        self.assertEqual(hd.certifier_last_name, '')
        self.assertEqual(hd.effective_date, datetime.datetime(year=1999, month=5, day=18))
        self.assertEqual(hd.last_action_date, datetime.datetime(year=2003, month=12, day=9))

    def test_kg0w_active(self):
        en_parse = EN('EN|2867281|||KG0W|L|L00170412|KASSAWARA, MATTHEW S|MATTHEW|S|KASSAWARA|||||1681 W Canal Cir Unit 121|Littleton|CO|80120|||000|0002451524|I|||')
        en_parse.get_object().save()

        hd_obj = HD('HD|2867281|||KG0W|A|HV|12/15/2006|12/15/2016||||||||||||||||||||N||Matthew|S|Kassawara||||||||||08/31/2011|08/31/2011||||||')
        self.assertEqual(hd_obj.unique_system_identifier, str(en_parse.get_object().unique_system_identifier))
        self.assertEqual(hd_obj.uls_file_number, '')
        self.assertEqual(hd_obj.call_sign, 'KG0W')
        self.assertEqual(hd_obj.license_status, 'A')
        self.assertEqual(hd_obj.radio_service_code, 'HV')
        self.assertEqual(hd_obj.grant_date, datetime.datetime(year=2006, month=12, day=15))
        self.assertEqual(hd_obj.expired_date, datetime.datetime(year=2016, month=12, day=15))
        self.assertEqual(hd_obj.cancellation_date, None)
        self.assertEqual(hd_obj.effective_date, datetime.datetime(year=2011, month=8, day=31))
        self.assertEqual(hd_obj.last_action_date, datetime.datetime(year=2011, month=8, day=31))

        en_obj = en.objects.get(unique_system_identifier='2867281')
        hd = hd_obj.get_object()
        self.assertEqual(hd.record_type, 'HD')
        self.assertEqual(hd.unique_system_identifier, en_obj)
        self.assertEqual(hd.uls_file_number, '')
        self.assertEqual(hd.call_sign, 'KG0W')
        self.assertEqual(hd.license_status, 'A')
        self.assertEqual(hd.radio_service_code, 'HV')
        self.assertEqual(hd.grant_date, datetime.datetime(year=2006, month=12, day=15))
        self.assertEqual(hd.expired_date, datetime.datetime(year=2016, month=12, day=15))
        self.assertEqual(hd.developmental_sta_demonstration, 'N')
        self.assertEqual(hd.certifier_first_name, 'Matthew')
        self.assertEqual(hd.certifier_mi, 'S')
        self.assertEqual(hd.certifier_last_name, 'Kassawara')
        self.assertEqual(hd.effective_date, datetime.datetime(year=2011, month=8, day=31))
        self.assertEqual(hd.last_action_date, datetime.datetime(year=2011, month=8, day=31))
