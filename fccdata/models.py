from django.db import models

class en(models.Model):
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

    class Meta:
        db_table = 'fcc_en'
        verbose_name_plural = 'EN'

class am(models.Model):
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

    def operator_class_verbose(self):
        if self.operator_class == 'T':
            return 'Technician'
        elif self.operator_class == 'E':
            return 'Extra'
        elif self.operator_class == 'A':
            return 'Advanced'
        elif self.operator_class == 'G':
            return 'General'
        elif self.operator_class == 'N':
            return 'Novice'
        elif self.operator_class == 'P':
            return 'Technician Plus'
        else:
            return self.operator_class

    class Meta:
        db_table = 'fcc_am'
        verbose_name_plural = 'AM'

class hd(models.Model):
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

    class Meta:
        db_table = 'fcc_hd'
        verbose_name_plural = 'HD'
