# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LlxdxAccountingAccount(models.Model):
    rowid = models.BigAutoField(primary_key=True)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_pcg_version = models.ForeignKey('LlxdxAccountingSystem', models.DO_NOTHING, db_column='fk_pcg_version', to_field='pcg_version')
    pcg_type = models.CharField(max_length=20)
    account_number = models.CharField(max_length=32)
    account_parent = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255)
    labelshort = models.CharField(max_length=255, blank=True, null=True)
    fk_accounting_category = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    reconcilable = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_accounting_account'
        unique_together = (('account_number', 'entity', 'fk_pcg_version'),)


class LlxdxAccountingBookkeeping(models.Model):
    rowid = models.AutoField(primary_key=True)
    doc_date = models.DateField()
    doc_type = models.CharField(max_length=30)
    doc_ref = models.CharField(max_length=300)
    fk_doc = models.IntegerField()
    fk_docdet = models.IntegerField()
    thirdparty_code = models.CharField(max_length=32, blank=True, null=True)
    numero_compte = models.CharField(max_length=20, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    label_compte = models.CharField(max_length=255, blank=True, null=True)
    label_operation = models.CharField(max_length=255, blank=True, null=True)
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    sens = models.CharField(max_length=1, blank=True, null=True)
    multicurrency_amount = models.FloatField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=255, blank=True, null=True)
    lettering_code = models.CharField(max_length=255, blank=True, null=True)
    date_lettering = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    code_journal = models.CharField(max_length=32, blank=True, null=True)
    journal_label = models.CharField(max_length=255, blank=True, null=True)
    piece_num = models.IntegerField()
    date_validated = models.DateTimeField(blank=True, null=True)
    date_export = models.DateTimeField(blank=True, null=True)
    entity = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    subledger_account = models.CharField(max_length=32, blank=True, null=True)
    subledger_label = models.CharField(max_length=255, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    date_lim_reglement = models.DateTimeField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_accounting_bookkeeping'


class LlxdxAccountingBookkeepingTmp(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    doc_date = models.DateField()
    doc_type = models.CharField(max_length=30)
    doc_ref = models.CharField(max_length=300)
    fk_doc = models.IntegerField()
    fk_docdet = models.IntegerField()
    thirdparty_code = models.CharField(max_length=32, blank=True, null=True)
    subledger_account = models.CharField(max_length=32, blank=True, null=True)
    subledger_label = models.CharField(max_length=255, blank=True, null=True)
    numero_compte = models.CharField(max_length=32, blank=True, null=True)
    label_compte = models.CharField(max_length=255)
    label_operation = models.CharField(max_length=255, blank=True, null=True)
    debit = models.FloatField()
    credit = models.FloatField()
    montant = models.FloatField()
    sens = models.CharField(max_length=1, blank=True, null=True)
    multicurrency_amount = models.FloatField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=255, blank=True, null=True)
    lettering_code = models.CharField(max_length=255, blank=True, null=True)
    date_lettering = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    code_journal = models.CharField(max_length=32)
    journal_label = models.CharField(max_length=255, blank=True, null=True)
    piece_num = models.IntegerField()
    date_validated = models.DateTimeField(blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    date_lim_reglement = models.DateTimeField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_accounting_bookkeeping_tmp'


class LlxdxAccountingFiscalyear(models.Model):
    rowid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=128)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    statut = models.IntegerField()
    entity = models.IntegerField()
    datec = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_accounting_fiscalyear'


class LlxdxAccountingGroupsAccount(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_accounting_account = models.IntegerField()
    fk_c_accounting_category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_accounting_groups_account'


class LlxdxAccountingJournal(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    label = models.CharField(max_length=128)
    nature = models.SmallIntegerField()
    active = models.SmallIntegerField(blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_accounting_journal'
        unique_together = (('code', 'entity'),)


class LlxdxAccountingSystem(models.Model):
    rowid = models.AutoField(primary_key=True)
    pcg_version = models.CharField(unique=True, max_length=32)
    label = models.CharField(max_length=128)
    active = models.SmallIntegerField(blank=True, null=True)
    fk_country = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_accounting_system'


class LlxdxActioncomm(models.Model):
    ref = models.CharField(max_length=30)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()
    datep = models.DateTimeField(blank=True, null=True)
    datep2 = models.DateTimeField(blank=True, null=True)
    fk_action = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_mod = models.IntegerField(blank=True, null=True)
    fk_project = models.IntegerField(blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_contact = models.IntegerField(blank=True, null=True)
    fk_parent = models.IntegerField()
    fk_user_action = models.IntegerField(blank=True, null=True)
    fk_user_done = models.IntegerField(blank=True, null=True)
    transparency = models.IntegerField(blank=True, null=True)
    priority = models.SmallIntegerField(blank=True, null=True)
    fulldayevent = models.SmallIntegerField()
    percent = models.SmallIntegerField()
    location = models.CharField(max_length=128, blank=True, null=True)
    durationp = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    email_subject = models.CharField(max_length=256, blank=True, null=True)
    email_msgid = models.CharField(max_length=256, blank=True, null=True)
    email_from = models.CharField(max_length=256, blank=True, null=True)
    email_sender = models.CharField(max_length=256, blank=True, null=True)
    email_to = models.CharField(max_length=256, blank=True, null=True)
    email_tocc = models.CharField(max_length=256, blank=True, null=True)
    email_tobcc = models.CharField(max_length=256, blank=True, null=True)
    errors_to = models.CharField(max_length=256, blank=True, null=True)
    recurid = models.CharField(max_length=128, blank=True, null=True)
    recurrule = models.CharField(max_length=128, blank=True, null=True)
    recurdateend = models.DateTimeField(blank=True, null=True)
    fk_element = models.IntegerField(blank=True, null=True)
    elementtype = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    calling_duration = models.IntegerField(blank=True, null=True)
    visibility = models.CharField(max_length=12, blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    num_vote = models.IntegerField(blank=True, null=True)
    event_paid = models.SmallIntegerField()
    status = models.SmallIntegerField()
    ip = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_actioncomm'


class LlxdxActioncommExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    obs1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_actioncomm_extrafields'


class LlxdxActioncommReminder(models.Model):
    rowid = models.AutoField(primary_key=True)
    dateremind = models.DateTimeField()
    typeremind = models.CharField(max_length=32)
    fk_user = models.IntegerField()
    offsetvalue = models.IntegerField()
    offsetunit = models.CharField(max_length=1)
    status = models.IntegerField()
    entity = models.IntegerField()
    fk_actioncomm = models.IntegerField()
    fk_email_template = models.IntegerField(blank=True, null=True)
    lasterror = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_actioncomm_reminder'
        unique_together = (('fk_user', 'typeremind', 'offsetvalue', 'offsetunit', 'fk_actioncomm'),)


class LlxdxActioncommResources(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_actioncomm = models.IntegerField()
    element_type = models.CharField(max_length=50)
    fk_element = models.IntegerField()
    answer_status = models.CharField(max_length=50, blank=True, null=True)
    mandatory = models.SmallIntegerField(blank=True, null=True)
    transparency = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_actioncomm_resources'
        unique_together = (('fk_actioncomm', 'element_type', 'fk_element'),)


class LlxdxAdherent(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=128, blank=True, null=True)
    civility = models.CharField(max_length=6, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    pass_crypted = models.CharField(max_length=128, blank=True, null=True)
    fk_adherent_type = models.ForeignKey('LlxdxAdherentType', models.DO_NOTHING, db_column='fk_adherent_type')
    morphy = models.CharField(max_length=3)
    societe = models.CharField(max_length=128, blank=True, null=True)
    fk_soc = models.OneToOneField('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zip = models.CharField(max_length=30, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    socialnetworks = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    phone_perso = models.CharField(max_length=30, blank=True, null=True)
    phone_mobile = models.CharField(max_length=30, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    statut = models.SmallIntegerField()
    public = models.SmallIntegerField()
    datefin = models.DateTimeField(blank=True, null=True)
    default_lang = models.CharField(max_length=6, blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    datevalid = models.DateTimeField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_mod = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    canvas = models.CharField(max_length=32, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_adherent'
        unique_together = (('login', 'entity'), ('ref', 'entity'),)


class LlxdxAdherentExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_adherent_extrafields'


class LlxdxAdherentType(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    tms = models.DateTimeField()
    statut = models.SmallIntegerField()
    libelle = models.CharField(max_length=50)
    subscription = models.CharField(max_length=3)
    amount = models.FloatField(blank=True, null=True)
    caneditamount = models.IntegerField(blank=True, null=True)
    vote = models.CharField(max_length=3)
    note = models.TextField(blank=True, null=True)
    mail_valid = models.TextField(blank=True, null=True)
    morphy = models.CharField(max_length=3, blank=True, null=True)
    duration = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_adherent_type'
        unique_together = (('libelle', 'entity'),)


class LlxdxAdherentTypeExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_adherent_type_extrafields'


class LlxdxAdherentTypeLang(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_type = models.IntegerField()
    lang = models.CharField(max_length=5)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_adherent_type_lang'


class LlxdxAsset(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    entity = models.IntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    fk_asset_model = models.ForeignKey('LlxdxAssetModel', models.DO_NOTHING, db_column='fk_asset_model', blank=True, null=True)
    reversal_amount_ht = models.FloatField(blank=True, null=True)
    acquisition_value_ht = models.FloatField()
    recovered_vat = models.FloatField(blank=True, null=True)
    reversal_date = models.DateField(blank=True, null=True)
    date_acquisition = models.DateField()
    date_start = models.DateField()
    qty = models.FloatField()
    acquisition_type = models.SmallIntegerField()
    asset_type = models.SmallIntegerField()
    not_depreciated = models.IntegerField(blank=True, null=True)
    disposal_date = models.DateField(blank=True, null=True)
    disposal_amount_ht = models.FloatField(blank=True, null=True)
    fk_disposal_type = models.ForeignKey('LlxdxCAssetDisposalType', models.DO_NOTHING, db_column='fk_disposal_type', blank=True, null=True)
    disposal_depreciated = models.IntegerField(blank=True, null=True)
    disposal_subject_to_vat = models.IntegerField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_modif', related_name='llxdxasset_fk_user_modif_set', blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_asset'


class LlxdxAssetAccountancyCodesEconomic(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_asset = models.OneToOneField(LlxdxAsset, models.DO_NOTHING, db_column='fk_asset', blank=True, null=True)
    fk_asset_model = models.OneToOneField('LlxdxAssetModel', models.DO_NOTHING, db_column='fk_asset_model', blank=True, null=True)
    asset = models.CharField(max_length=32, blank=True, null=True)
    depreciation_asset = models.CharField(max_length=32, blank=True, null=True)
    depreciation_expense = models.CharField(max_length=32, blank=True, null=True)
    value_asset_sold = models.CharField(max_length=32, blank=True, null=True)
    receivable_on_assignment = models.CharField(max_length=32, blank=True, null=True)
    proceeds_from_sales = models.CharField(max_length=32, blank=True, null=True)
    vat_collected = models.CharField(max_length=32, blank=True, null=True)
    vat_deductible = models.CharField(max_length=32, blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_modif = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_modif', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_asset_accountancy_codes_economic'


class LlxdxAssetAccountancyCodesFiscal(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_asset = models.OneToOneField(LlxdxAsset, models.DO_NOTHING, db_column='fk_asset', blank=True, null=True)
    fk_asset_model = models.OneToOneField('LlxdxAssetModel', models.DO_NOTHING, db_column='fk_asset_model', blank=True, null=True)
    accelerated_depreciation = models.CharField(max_length=32, blank=True, null=True)
    endowment_accelerated_depreciation = models.CharField(max_length=32, blank=True, null=True)
    provision_accelerated_depreciation = models.CharField(max_length=32, blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_modif = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_modif', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_asset_accountancy_codes_fiscal'


class LlxdxAssetDepreciation(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_asset = models.ForeignKey(LlxdxAsset, models.DO_NOTHING, db_column='fk_asset')
    depreciation_mode = models.CharField(max_length=255)
    ref = models.CharField(max_length=255)
    depreciation_date = models.DateTimeField()
    depreciation_ht = models.FloatField()
    cumulative_depreciation_ht = models.FloatField()
    accountancy_code_debit = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_credit = models.CharField(max_length=32, blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_modif = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_modif', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_asset_depreciation'
        unique_together = (('fk_asset', 'depreciation_mode', 'ref'),)


class LlxdxAssetDepreciationOptionsEconomic(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_asset = models.OneToOneField(LlxdxAsset, models.DO_NOTHING, db_column='fk_asset', blank=True, null=True)
    fk_asset_model = models.OneToOneField('LlxdxAssetModel', models.DO_NOTHING, db_column='fk_asset_model', blank=True, null=True)
    depreciation_type = models.SmallIntegerField()
    accelerated_depreciation_option = models.IntegerField(blank=True, null=True)
    degressive_coefficient = models.FloatField(blank=True, null=True)
    duration = models.SmallIntegerField()
    duration_type = models.SmallIntegerField()
    amount_base_depreciation_ht = models.FloatField(blank=True, null=True)
    amount_base_deductible_ht = models.FloatField(blank=True, null=True)
    total_amount_last_depreciation_ht = models.FloatField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_modif = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_modif', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_asset_depreciation_options_economic'


class LlxdxAssetDepreciationOptionsFiscal(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_asset = models.OneToOneField(LlxdxAsset, models.DO_NOTHING, db_column='fk_asset', blank=True, null=True)
    fk_asset_model = models.OneToOneField('LlxdxAssetModel', models.DO_NOTHING, db_column='fk_asset_model', blank=True, null=True)
    depreciation_type = models.SmallIntegerField()
    degressive_coefficient = models.FloatField(blank=True, null=True)
    duration = models.SmallIntegerField()
    duration_type = models.SmallIntegerField()
    amount_base_depreciation_ht = models.FloatField(blank=True, null=True)
    amount_base_deductible_ht = models.FloatField(blank=True, null=True)
    total_amount_last_depreciation_ht = models.FloatField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_modif = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_modif', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_asset_depreciation_options_fiscal'


class LlxdxAssetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_asset_extrafields'


class LlxdxAssetModel(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref = models.CharField(max_length=128)
    label = models.CharField(max_length=255)
    asset_type = models.SmallIntegerField()
    fk_pays = models.IntegerField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_modif', related_name='llxdxassetmodel_fk_user_modif_set', blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_asset_model'
        unique_together = (('entity', 'ref'),)


class LlxdxAssetModelExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_asset_model_extrafields'


class LlxdxBank(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datev = models.DateField(blank=True, null=True)
    dateo = models.DateField(blank=True, null=True)
    amount = models.FloatField()
    label = models.CharField(max_length=255, blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_rappro = models.IntegerField(blank=True, null=True)
    fk_type = models.CharField(max_length=6, blank=True, null=True)
    num_releve = models.CharField(max_length=50, blank=True, null=True)
    num_chq = models.CharField(max_length=50, blank=True, null=True)
    rappro = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_bordereau = models.IntegerField(blank=True, null=True)
    banque = models.CharField(max_length=255, blank=True, null=True)
    emetteur = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)
    numero_compte = models.CharField(max_length=32, blank=True, null=True)
    origin_id = models.IntegerField(blank=True, null=True)
    origin_type = models.CharField(max_length=64, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    amount_main_currency = models.FloatField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bank'


class LlxdxBankAccount(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    ref = models.CharField(max_length=12)
    label = models.CharField(max_length=30)
    entity = models.IntegerField()
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    bank = models.CharField(max_length=60, blank=True, null=True)
    code_banque = models.CharField(max_length=128, blank=True, null=True)
    code_guichet = models.CharField(max_length=6, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    cle_rib = models.CharField(max_length=5, blank=True, null=True)
    bic = models.CharField(max_length=11, blank=True, null=True)
    iban_prefix = models.CharField(max_length=34, blank=True, null=True)
    country_iban = models.CharField(max_length=2, blank=True, null=True)
    cle_iban = models.CharField(max_length=2, blank=True, null=True)
    domiciliation = models.CharField(max_length=255, blank=True, null=True)
    pti_in_ctti = models.SmallIntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    fk_pays = models.IntegerField()
    proprio = models.CharField(max_length=60, blank=True, null=True)
    owner_address = models.CharField(max_length=255, blank=True, null=True)
    courant = models.SmallIntegerField()
    clos = models.SmallIntegerField()
    rappro = models.SmallIntegerField(blank=True, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)
    account_number = models.CharField(max_length=32, blank=True, null=True)
    accountancy_journal = models.CharField(max_length=20, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    min_allowed = models.IntegerField(blank=True, null=True)
    min_desired = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_accountancy_journal = models.ForeignKey(LlxdxAccountingJournal, models.DO_NOTHING, db_column='fk_accountancy_journal', blank=True, null=True)
    ics = models.CharField(max_length=32, blank=True, null=True)
    ics_transfer = models.CharField(max_length=32, blank=True, null=True)
    owner_zip = models.CharField(max_length=25, blank=True, null=True)
    owner_town = models.CharField(max_length=50, blank=True, null=True)
    owner_country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bank_account'
        unique_together = (('label', 'entity'),)


class LlxdxBankAccountExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bank_account_extrafields'


class LlxdxBankCateg(models.Model):
    rowid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_bank_categ'


class LlxdxBankClass(models.Model):
    lineid = models.IntegerField()
    fk_categ = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_bank_class'
        unique_together = (('lineid', 'fk_categ'),)


class LlxdxBankExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bank_extrafields'


class LlxdxBankUrl(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_bank = models.IntegerField(blank=True, null=True)
    url_id = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'llxdx_bank_url'
        unique_together = (('fk_bank', 'url_id', 'type'),)


class LlxdxBlockedlog(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    action = models.CharField(max_length=50, blank=True, null=True)
    amounts = models.FloatField()
    signature = models.CharField(max_length=100)
    signature_line = models.CharField(max_length=100)
    element = models.CharField(max_length=50, blank=True, null=True)
    fk_object = models.IntegerField(blank=True, null=True)
    ref_object = models.CharField(max_length=255, blank=True, null=True)
    date_object = models.DateTimeField(blank=True, null=True)
    object_data = models.TextField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField()
    certified = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    user_fullname = models.CharField(max_length=255, blank=True, null=True)
    object_version = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_blockedlog'


class LlxdxBlockedlogAuthority(models.Model):
    rowid = models.AutoField(primary_key=True)
    blockchain = models.TextField()
    signature = models.CharField(max_length=100)
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_blockedlog_authority'


class LlxdxBomBom(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref = models.CharField(max_length=128)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    efficiency = models.FloatField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    date_valid = models.DateTimeField(blank=True, null=True)
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.IntegerField()
    duration = models.FloatField(blank=True, null=True)
    fk_warehouse = models.IntegerField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    bomtype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bom_bom'
        unique_together = (('ref', 'entity'),)


class LlxdxBomBomExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bom_bom_extrafields'


class LlxdxBomBomline(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_bom = models.ForeignKey(LlxdxBomBom, models.DO_NOTHING, db_column='fk_bom')
    fk_product = models.IntegerField()
    fk_bom_child = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    qty = models.FloatField()
    efficiency = models.FloatField()
    position = models.IntegerField()
    qty_frozen = models.SmallIntegerField(blank=True, null=True)
    disable_stock_change = models.SmallIntegerField(blank=True, null=True)
    fk_unit = models.IntegerField(blank=True, null=True)
    fk_default_workstation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bom_bomline'


class LlxdxBomBomlineExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bom_bomline_extrafields'


class LlxdxBookmark(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_user = models.IntegerField()
    dateb = models.DateTimeField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    target = models.CharField(max_length=16, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    favicon = models.CharField(max_length=24, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_bookmark'
        unique_together = (('fk_user', 'entity', 'title'),)


class LlxdxBordereauCheque(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    label = models.CharField(max_length=255, blank=True, null=True)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    datec = models.DateTimeField()
    date_bordereau = models.DateField(blank=True, null=True)
    amount = models.FloatField()
    nbcheque = models.SmallIntegerField()
    fk_bank_account = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    statut = models.SmallIntegerField()
    tms = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    entity = models.IntegerField()
    type = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_bordereau_cheque'
        unique_together = (('ref', 'entity'),)


class LlxdxBoxes(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    box = models.ForeignKey('LlxdxBoxesDef', models.DO_NOTHING)
    position = models.SmallIntegerField()
    box_order = models.CharField(max_length=3)
    fk_user = models.IntegerField()
    maxline = models.IntegerField(blank=True, null=True)
    params = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_boxes'
        unique_together = (('entity', 'box', 'position', 'fk_user'),)


class LlxdxBoxesDef(models.Model):
    rowid = models.AutoField(primary_key=True)
    file = models.CharField(max_length=200)
    entity = models.IntegerField()
    tms = models.DateTimeField()
    note = models.CharField(max_length=130, blank=True, null=True)
    fk_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_boxes_def'
        unique_together = (('file', 'entity', 'note'),)


class LlxdxBudget(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    label = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_budget'


class LlxdxBudgetLines(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_budget = models.ForeignKey(LlxdxBudget, models.DO_NOTHING, db_column='fk_budget')
    fk_project_ids = models.CharField(max_length=255)
    amount = models.FloatField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_budget_lines'
        unique_together = (('fk_budget', 'fk_project_ids'),)


class LlxdxCAccountingCategory(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    code = models.CharField(max_length=16)
    label = models.CharField(max_length=255)
    range_account = models.CharField(max_length=255)
    sens = models.IntegerField()
    category_type = models.IntegerField()
    formula = models.CharField(max_length=255)
    position = models.IntegerField(blank=True, null=True)
    fk_country = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_accounting_category'
        unique_together = (('code', 'entity'),)


class LlxdxCActionTrigger(models.Model):
    rowid = models.AutoField(primary_key=True)
    elementtype = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(unique=True, max_length=128, blank=True, null=True)
    label = models.CharField(max_length=128)
    description = models.CharField(max_length=255, blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    contexts = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_action_trigger'


class LlxdxCActioncomm(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=50)
    type = models.CharField(max_length=50)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField()
    todo = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=9, blank=True, null=True)
    position = models.IntegerField()
    picto = models.CharField(max_length=48, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_actioncomm'


class LlxdxCAssetDisposalType(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    code = models.CharField(max_length=16)
    label = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_asset_disposal_type'
        unique_together = (('code', 'entity'),)


class LlxdxCAvailability(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=30)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    position = models.IntegerField()
    type_duration = models.CharField(max_length=1, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_availability'


class LlxdxCBarcodeType(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=16)
    entity = models.IntegerField()
    libelle = models.CharField(max_length=128, blank=True, null=True)
    coder = models.CharField(max_length=16)
    example = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'llxdx_c_barcode_type'
        unique_together = (('code', 'entity'),)


class LlxdxCChargesociales(models.Model):
    libelle = models.CharField(max_length=128, blank=True, null=True)
    deductible = models.SmallIntegerField()
    active = models.IntegerField()
    code = models.CharField(max_length=12)
    accountancy_code = models.CharField(max_length=32, blank=True, null=True)
    fk_pays = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_chargesociales'


class LlxdxCCivility(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=6)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_civility'


class LlxdxCCountry(models.Model):
    rowid = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=2)
    code_iso = models.CharField(unique=True, max_length=3, blank=True, null=True)
    label = models.CharField(unique=True, max_length=128, blank=True, null=True)
    active = models.IntegerField()
    favorite = models.IntegerField()
    eec = models.IntegerField()
    numeric_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_country'


class LlxdxCCurrencies(models.Model):
    code_iso = models.CharField(primary_key=True, max_length=3)
    label = models.CharField(max_length=128, blank=True, null=True)
    unicode = models.CharField(max_length=32, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_currencies'


class LlxdxCDepartements(models.Model):
    rowid = models.AutoField(primary_key=True)
    code_departement = models.CharField(max_length=6)
    fk_region = models.ForeignKey('LlxdxCRegions', models.DO_NOTHING, db_column='fk_region', to_field='code_region', blank=True, null=True)
    cheflieu = models.CharField(max_length=50, blank=True, null=True)
    tncc = models.IntegerField(blank=True, null=True)
    ncc = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_departements'
        unique_together = (('code_departement', 'fk_region'),)


class LlxdxCEcotaxe(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=64)
    label = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    fk_pays = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_ecotaxe'


class LlxdxCEffectif(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=12)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_effectif'


class LlxdxCEmailSenderprofile(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    private = models.SmallIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    label = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    position = models.SmallIntegerField(blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_email_senderprofile'
        unique_together = (('entity', 'label', 'email'),)


class LlxdxCEmailTemplates(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)
    type_template = models.CharField(max_length=32, blank=True, null=True)
    lang = models.CharField(max_length=6, blank=True, null=True)
    private = models.SmallIntegerField()
    fk_user = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    label = models.CharField(max_length=255, blank=True, null=True)
    position = models.SmallIntegerField(blank=True, null=True)
    active = models.IntegerField()
    topic = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_lines = models.TextField(blank=True, null=True)
    enabled = models.CharField(max_length=255, blank=True, null=True)
    joinfiles = models.CharField(max_length=255, blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    email_to = models.CharField(max_length=255, blank=True, null=True)
    email_tocc = models.CharField(max_length=255, blank=True, null=True)
    email_tobcc = models.CharField(max_length=255, blank=True, null=True)
    defaultfortype = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_email_templates'
        unique_together = (('entity', 'label', 'lang'),)


class LlxdxCExpTaxCat(models.Model):
    rowid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=128, blank=True, null=True)
    entity = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_exp_tax_cat'


class LlxdxCExpTaxRange(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_c_exp_tax_cat = models.IntegerField()
    range_ik = models.FloatField()
    entity = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_exp_tax_range'


class LlxdxCFieldList(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    element = models.CharField(max_length=64)
    entity = models.IntegerField()
    name = models.CharField(max_length=32)
    alias = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    align = models.CharField(max_length=6, blank=True, null=True)
    sort = models.IntegerField()
    search = models.IntegerField()
    visible = models.IntegerField()
    enabled = models.CharField(max_length=255, blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_field_list'


class LlxdxCFormatCards(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    paper_size = models.CharField(max_length=20)
    orientation = models.CharField(max_length=1)
    metric = models.CharField(max_length=5)
    leftmargin = models.FloatField()
    topmargin = models.FloatField()
    nx = models.IntegerField()
    ny = models.IntegerField()
    spacex = models.FloatField()
    spacey = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    font_size = models.IntegerField()
    custom_x = models.FloatField()
    custom_y = models.FloatField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_format_cards'


class LlxdxCFormeJuridique(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.IntegerField(unique=True)
    fk_pays = models.IntegerField()
    libelle = models.CharField(max_length=255, blank=True, null=True)
    isvatexempted = models.IntegerField()
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_forme_juridique'


class LlxdxCHolidayTypes(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=16)
    label = models.CharField(max_length=255)
    affect = models.IntegerField()
    delay = models.IntegerField()
    newbymonth = models.FloatField()
    fk_country = models.IntegerField(blank=True, null=True)
    block_if_negative = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_holiday_types'


class LlxdxCHrmDepartment(models.Model):
    rowid = models.IntegerField(primary_key=True)
    pos = models.IntegerField()
    code = models.CharField(max_length=16)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_hrm_department'


class LlxdxCHrmFunction(models.Model):
    rowid = models.IntegerField(primary_key=True)
    pos = models.IntegerField()
    code = models.CharField(max_length=16)
    label = models.CharField(max_length=128, blank=True, null=True)
    c_level = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_hrm_function'


class LlxdxCHrmPublicHoliday(models.Model):
    entity = models.IntegerField()
    fk_country = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=62, blank=True, null=True)
    dayrule = models.CharField(max_length=64, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_hrm_public_holiday'
        unique_together = (('entity', 'code'), ('entity', 'fk_country', 'dayrule', 'day', 'month', 'year'),)


class LlxdxCIncoterms(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=3)
    libelle = models.CharField(max_length=255)
    active = models.IntegerField()
    label = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_incoterms'


class LlxdxCInputMethod(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=30, blank=True, null=True)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_input_method'


class LlxdxCInputReason(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=30, blank=True, null=True)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_input_reason'


class LlxdxCInvoiceSubtype(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    fk_country = models.IntegerField()
    code = models.CharField(max_length=4, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_invoice_subtype'
        unique_together = (('entity', 'code'),)


class LlxdxCLeadStatus(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=10, blank=True, null=True)
    label = models.CharField(max_length=128, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_lead_status'


class LlxdxCPaiement(models.Model):
    entity = models.IntegerField()
    code = models.CharField(max_length=6)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    active = models.IntegerField()
    accountancy_code = models.CharField(max_length=32, blank=True, null=True)
    module = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_paiement'
        unique_together = (('entity', 'code'),)


class LlxdxCPaiementTemp(models.Model):
    idLlxdx = models.IntegerField() #Puse este id ya que : read_original_db.LlxdxCPaiementTemp: (models.E004) 'id' can only be used as a field name if the field also sets 'primary_key=True'.
    entity = models.IntegerField()
    code = models.CharField(max_length=6, db_collation='utf8mb3_general_ci')
    libelle = models.CharField(max_length=62, db_collation='utf8mb3_general_ci', blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    active = models.IntegerField()
    accountancy_code = models.CharField(max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)
    module = models.CharField(max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_paiement_temp'


class LlxdxCPaperFormat(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=16)
    label = models.CharField(max_length=128, blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=5)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_paper_format'


class LlxdxCPartnershipType(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    code = models.CharField(max_length=32)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    keyword = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_partnership_type'
        unique_together = (('entity', 'code'),)


class LlxdxCPaymentTerm(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    code = models.CharField(max_length=16, blank=True, null=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    libelle_facture = models.TextField(blank=True, null=True)
    type_cdr = models.IntegerField(blank=True, null=True)
    nbjour = models.SmallIntegerField(blank=True, null=True)
    decalage = models.SmallIntegerField(blank=True, null=True)
    deposit_percent = models.CharField(max_length=63, blank=True, null=True)
    module = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_payment_term'
        unique_together = (('entity', 'code'),)


class LlxdxCPriceExpression(models.Model):
    rowid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    expression = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'llxdx_c_price_expression'


class LlxdxCPriceGlobalVariable(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_price_global_variable'


class LlxdxCPriceGlobalVariableUpdater(models.Model):
    rowid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    fk_variable = models.IntegerField()
    update_interval = models.IntegerField(blank=True, null=True)
    next_update = models.IntegerField(blank=True, null=True)
    last_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_price_global_variable_updater'


class LlxdxCProductNature(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.IntegerField(unique=True)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_product_nature'


class LlxdxCProductbatchQcstatus(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    code = models.CharField(max_length=16)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_productbatch_qcstatus'
        unique_together = (('code', 'entity'),)


class LlxdxCPropalst(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=12)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    sortorder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_propalst'


class LlxdxCProspectcontactlevel(models.Model):
    code = models.CharField(primary_key=True, max_length=12)
    label = models.CharField(max_length=128, blank=True, null=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    active = models.SmallIntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_prospectcontactlevel'


class LlxdxCProspectlevel(models.Model):
    code = models.CharField(primary_key=True, max_length=12)
    label = models.CharField(max_length=128, blank=True, null=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    active = models.SmallIntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_prospectlevel'


class LlxdxCRecruitmentOrigin(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_recruitment_origin'


class LlxdxCRegions(models.Model):
    rowid = models.AutoField(primary_key=True)
    code_region = models.IntegerField(unique=True)
    fk_pays = models.IntegerField()
    cheflieu = models.CharField(max_length=50, blank=True, null=True)
    tncc = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_regions'


class LlxdxCRevenuestamp(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_pays = models.IntegerField()
    taux = models.FloatField()
    note = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    accountancy_code_sell = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy = models.CharField(max_length=32, blank=True, null=True)
    revenuestamp_type = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'llxdx_c_revenuestamp'


class LlxdxCShipmentMode(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    code = models.CharField(max_length=30)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tracking = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=32, blank=True, null=True)
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_shipment_mode'
        unique_together = (('code', 'entity'),)


class LlxdxCShipmentPackageType(models.Model):
    rowid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_shipment_package_type'


class LlxdxCSocialnetworks(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    code = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=150, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=20, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_socialnetworks'
        unique_together = (('code', 'entity'),)


class LlxdxCStcomm(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=24)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    picto = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    sortorder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_stcomm'


class LlxdxCStcommcontact(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=12)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    picto = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_stcommcontact'


class LlxdxCTicketCategory(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=32)
    pos = models.IntegerField()
    label = models.CharField(max_length=128)
    active = models.IntegerField(blank=True, null=True)
    use_default = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_parent = models.IntegerField()
    force_severity = models.CharField(max_length=32, blank=True, null=True)
    public = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_ticket_category'
        unique_together = (('code', 'entity'),)


class LlxdxCTicketResolution(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=32)
    pos = models.CharField(max_length=32)
    label = models.CharField(max_length=128)
    active = models.IntegerField(blank=True, null=True)
    use_default = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_ticket_resolution'
        unique_together = (('code', 'entity'),)


class LlxdxCTicketSeverity(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=32)
    pos = models.CharField(max_length=32)
    label = models.CharField(max_length=128)
    color = models.CharField(max_length=10, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    use_default = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_ticket_severity'
        unique_together = (('code', 'entity'),)


class LlxdxCTicketType(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=32)
    pos = models.CharField(max_length=32)
    label = models.CharField(max_length=128)
    active = models.IntegerField(blank=True, null=True)
    use_default = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_ticket_type'
        unique_together = (('code', 'entity'),)


class LlxdxCTransportMode(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    code = models.CharField(max_length=3)
    label = models.CharField(max_length=255)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_transport_mode'
        unique_together = (('code', 'entity'),)


class LlxdxCTva(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_pays = models.IntegerField()
    code = models.CharField(max_length=10, blank=True, null=True)
    taux = models.FloatField()
    localtax1 = models.CharField(max_length=20)
    localtax1_type = models.CharField(max_length=10)
    localtax2 = models.CharField(max_length=20)
    localtax2_type = models.CharField(max_length=10)
    recuperableonly = models.IntegerField()
    note = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    accountancy_code_sell = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy = models.CharField(max_length=32, blank=True, null=True)
    use_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_tva'
        unique_together = (('fk_pays', 'code', 'taux', 'recuperableonly'),)


class LlxdxCTypeContact(models.Model):
    rowid = models.AutoField(primary_key=True)
    element = models.CharField(max_length=30)
    source = models.CharField(max_length=8)
    code = models.CharField(max_length=32)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_type_contact'
        unique_together = (('element', 'source', 'code'),)


class LlxdxCTypeContainer(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    entity = models.IntegerField()
    label = models.CharField(max_length=128, blank=True, null=True)
    module = models.CharField(max_length=32, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_type_container'
        unique_together = (('code', 'entity'),)


class LlxdxCTypeFees(models.Model):
    code = models.CharField(unique=True, max_length=12)
    label = models.CharField(max_length=128, blank=True, null=True)
    accountancy_code = models.CharField(max_length=32, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_type_fees'


class LlxdxCTypeResource(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    label = models.CharField(max_length=128, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_type_resource'
        unique_together = (('label', 'code'),)


class LlxdxCTypent(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=12)
    libelle = models.CharField(max_length=128, blank=True, null=True)
    fk_country = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    module = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_c_typent'


class LlxdxCUnits(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=3, blank=True, null=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    label = models.CharField(max_length=128, blank=True, null=True)
    short_label = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField()
    scale = models.IntegerField(blank=True, null=True)
    unit_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_units'


class LlxdxCZiptown(models.Model):
    rowid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    fk_county = models.ForeignKey(LlxdxCDepartements, models.DO_NOTHING, db_column='fk_county', blank=True, null=True)
    fk_pays = models.ForeignKey(LlxdxCCountry, models.DO_NOTHING, db_column='fk_pays')
    zip = models.CharField(max_length=10)
    town = models.CharField(max_length=255)
    active = models.IntegerField()
    town_up = models.CharField(max_length=180, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_c_ziptown'
        unique_together = (('zip', 'town', 'fk_pays'),)


class LlxdxCategorie(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_parent = models.IntegerField()
    label = models.CharField(max_length=255)
    type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=8, blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie'
        unique_together = (('entity', 'fk_parent', 'label', 'type'),)


class LlxdxCategorieAccount(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_account) found, that is not supported. The first column is selected.
    fk_account = models.ForeignKey(LlxdxBankAccount, models.DO_NOTHING, db_column='fk_account')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_account'
        unique_together = (('fk_categorie', 'fk_account'),)


class LlxdxCategorieActioncomm(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_actioncomm) found, that is not supported. The first column is selected.
    fk_actioncomm = models.ForeignKey(LlxdxActioncomm, models.DO_NOTHING, db_column='fk_actioncomm')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_actioncomm'
        unique_together = (('fk_categorie', 'fk_actioncomm'),)


class LlxdxCategorieContact(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_socpeople) found, that is not supported. The first column is selected.
    fk_socpeople = models.ForeignKey('LlxdxSocpeople', models.DO_NOTHING, db_column='fk_socpeople')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_contact'
        unique_together = (('fk_categorie', 'fk_socpeople'),)


class LlxdxCategorieFournisseur(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_soc) found, that is not supported. The first column is selected.
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_fournisseur'
        unique_together = (('fk_categorie', 'fk_soc'),)


class LlxdxCategorieKnowledgemanagement(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_knowledgemanagement) found, that is not supported. The first column is selected.
    fk_knowledgemanagement = models.ForeignKey('LlxdxKnowledgemanagementKnowledgerecord', models.DO_NOTHING, db_column='fk_knowledgemanagement')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_knowledgemanagement'
        unique_together = (('fk_categorie', 'fk_knowledgemanagement'),)


class LlxdxCategorieLang(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_category = models.ForeignKey(LlxdxCategorie, models.DO_NOTHING, db_column='fk_category')
    lang = models.CharField(max_length=5)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_lang'
        unique_together = (('fk_category', 'lang'),)


class LlxdxCategorieMember(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_member) found, that is not supported. The first column is selected.
    fk_member = models.ForeignKey(LlxdxAdherent, models.DO_NOTHING, db_column='fk_member')

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_member'
        unique_together = (('fk_categorie', 'fk_member'),)


class LlxdxCategorieProduct(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_product) found, that is not supported. The first column is selected.
    fk_product = models.ForeignKey('LlxdxProduct', models.DO_NOTHING, db_column='fk_product')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_product'
        unique_together = (('fk_categorie', 'fk_product'),)


class LlxdxCategorieProject(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_project) found, that is not supported. The first column is selected.
    fk_project = models.ForeignKey('LlxdxProjet', models.DO_NOTHING, db_column='fk_project')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_project'
        unique_together = (('fk_categorie', 'fk_project'),)


class LlxdxCategorieSociete(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_soc) found, that is not supported. The first column is selected.
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_societe'
        unique_together = (('fk_categorie', 'fk_soc'),)


class LlxdxCategorieTicket(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_ticket) found, that is not supported. The first column is selected.
    fk_ticket = models.ForeignKey('LlxdxTicket', models.DO_NOTHING, db_column='fk_ticket')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_ticket'
        unique_together = (('fk_categorie', 'fk_ticket'),)


class LlxdxCategorieUser(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_user) found, that is not supported. The first column is selected.
    fk_user = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_user'
        unique_together = (('fk_categorie', 'fk_user'),)


class LlxdxCategorieWarehouse(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_warehouse) found, that is not supported. The first column is selected.
    fk_warehouse = models.ForeignKey('LlxdxEntrepot', models.DO_NOTHING, db_column='fk_warehouse')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_warehouse'
        unique_together = (('fk_categorie', 'fk_warehouse'),)


class LlxdxCategorieWebsitePage(models.Model):
    fk_categorie = models.OneToOneField(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', primary_key=True)  # The composite primary key (fk_categorie, fk_website_page) found, that is not supported. The first column is selected.
    fk_website_page = models.ForeignKey('LlxdxWebsitePage', models.DO_NOTHING, db_column='fk_website_page')
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categorie_website_page'
        unique_together = (('fk_categorie', 'fk_website_page'),)


class LlxdxCategoriesExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_categories_extrafields'


class LlxdxChargesociales(models.Model):
    rowid = models.AutoField(primary_key=True)
    date_ech = models.DateTimeField()
    libelle = models.CharField(max_length=80)
    entity = models.IntegerField()
    tms = models.DateTimeField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    fk_type = models.IntegerField()
    fk_account = models.IntegerField(blank=True, null=True)
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    paye = models.SmallIntegerField()
    periode = models.DateField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=16, blank=True, null=True)
    fk_projet = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_chargesociales'


class LlxdxCommande(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_int = models.CharField(max_length=255, blank=True, null=True)
    ref_client = models.CharField(max_length=255, blank=True, null=True)
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    fk_projet = models.ForeignKey('LlxdxProjet', models.DO_NOTHING, db_column='fk_projet', blank=True, null=True)
    tms = models.DateTimeField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    date_cloture = models.DateTimeField(blank=True, null=True)
    date_commande = models.DateField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_valid', related_name='llxdxcommande_fk_user_valid_set', blank=True, null=True)
    fk_user_cloture = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_cloture', related_name='llxdxcommande_fk_user_cloture_set', blank=True, null=True)
    source = models.SmallIntegerField(blank=True, null=True)
    fk_statut = models.SmallIntegerField(blank=True, null=True)
    amount_ht = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise_absolue = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    revenuestamp = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    facture = models.IntegerField(blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_currency = models.CharField(max_length=3, blank=True, null=True)
    fk_cond_reglement = models.IntegerField(blank=True, null=True)
    deposit_percent = models.CharField(max_length=63, blank=True, null=True)
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    date_livraison = models.DateTimeField(blank=True, null=True)
    fk_shipping_method = models.IntegerField(blank=True, null=True)
    fk_warehouse = models.IntegerField(blank=True, null=True)
    fk_availability = models.IntegerField(blank=True, null=True)
    fk_input_reason = models.IntegerField(blank=True, null=True)
    fk_delivery_address = models.IntegerField(blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    module_source = models.CharField(max_length=32, blank=True, null=True)
    pos_source = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande'
        unique_together = (('ref', 'entity'),)


class LlxdxCommandeExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_extrafields'


class LlxdxCommandeFournisseur(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=255)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=64, blank=True, null=True)
    ref_supplier = models.CharField(max_length=255, blank=True, null=True)
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    fk_projet = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    date_approve = models.DateTimeField(blank=True, null=True)
    date_approve2 = models.DateTimeField(blank=True, null=True)
    date_commande = models.DateField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    fk_user_approve = models.IntegerField(blank=True, null=True)
    fk_user_approve2 = models.IntegerField(blank=True, null=True)
    source = models.SmallIntegerField()
    fk_statut = models.SmallIntegerField(blank=True, null=True)
    billed = models.SmallIntegerField(blank=True, null=True)
    amount_ht = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    date_livraison = models.DateTimeField(blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_cond_reglement = models.IntegerField(blank=True, null=True)
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    fk_input_method = models.IntegerField(blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_fournisseur'
        unique_together = (('ref', 'entity'),)


class LlxdxCommandeFournisseurDispatch(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_commande = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    fk_commandefourndet = models.IntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    fk_entrepot = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    batch = models.CharField(max_length=128, blank=True, null=True)
    eatby = models.DateField(blank=True, null=True)
    sellby = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_projet = models.IntegerField(blank=True, null=True)
    fk_reception = models.IntegerField(blank=True, null=True)
    cost_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_fournisseur_dispatch'


class LlxdxCommandeFournisseurDispatchExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_fournisseur_dispatch_extrafields'


class LlxdxCommandeFournisseurExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    oc1 = models.CharField(unique=True, max_length=255, blank=True, null=True)
    sol1 = models.CharField(max_length=255, blank=True, null=True)
    form1 = models.CharField(max_length=255, blank=True, null=True)
    fech1 = models.DateField(blank=True, null=True)
    pos1 = models.IntegerField(blank=True, null=True)
    obsnc = models.CharField(max_length=255, blank=True, null=True)
    fecharecepciontotal = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_fournisseur_extrafields'


class LlxdxCommandeFournisseurLog(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    datelog = models.DateTimeField()
    fk_commande = models.IntegerField()
    fk_statut = models.SmallIntegerField()
    fk_user = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_fournisseur_log'


class LlxdxCommandeFournisseurdet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_commande = models.IntegerField()
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=128, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    special_code = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_fournisseurdet'


class LlxdxCommandeFournisseurdetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commande_fournisseurdet_extrafields'


class LlxdxCommandedet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_commande = models.ForeignKey(LlxdxCommande, models.DO_NOTHING, db_column='fk_commande')
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    buy_price_ht = models.FloatField(blank=True, null=True)
    fk_product_fournisseur_price = models.IntegerField(blank=True, null=True)
    special_code = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_commandefourndet = models.ForeignKey(LlxdxCommandeFournisseurdet, models.DO_NOTHING, db_column='fk_commandefourndet', blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commandedet'


class LlxdxCommandedetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_commandedet_extrafields'


class LlxdxComment(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    description = models.TextField()
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_element = models.IntegerField(blank=True, null=True)
    element_type = models.CharField(max_length=50, blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=125, blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_comment'


class LlxdxConst(models.Model):
    rowid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    entity = models.IntegerField()
    value = models.TextField()
    type = models.CharField(max_length=64, blank=True, null=True)
    visible = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_const'
        unique_together = (('name', 'entity'),)


class LlxdxContrat(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=50, blank=True, null=True)
    ref_customer = models.CharField(max_length=50, blank=True, null=True)
    ref_supplier = models.CharField(max_length=50, blank=True, null=True)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    date_contrat = models.DateTimeField(blank=True, null=True)
    statut = models.SmallIntegerField(blank=True, null=True)
    mise_en_service = models.DateTimeField(blank=True, null=True)
    fin_validite = models.DateTimeField(blank=True, null=True)
    date_cloture = models.DateTimeField(blank=True, null=True)
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    fk_projet = models.IntegerField(blank=True, null=True)
    fk_commercial_signature = models.IntegerField(blank=True, null=True)
    fk_commercial_suivi = models.IntegerField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author')
    fk_user_mise_en_service = models.IntegerField(blank=True, null=True)
    fk_user_cloture = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_contrat'
        unique_together = (('ref', 'entity'),)


class LlxdxContratExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_contrat_extrafields'


class LlxdxContratdet(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_contrat = models.ForeignKey(LlxdxContrat, models.DO_NOTHING, db_column='fk_contrat')
    fk_product = models.ForeignKey('LlxdxProduct', models.DO_NOTHING, db_column='fk_product', blank=True, null=True)
    statut = models.SmallIntegerField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    date_commande = models.DateTimeField(blank=True, null=True)
    date_ouverture_prevue = models.DateTimeField(blank=True, null=True)
    date_ouverture = models.DateTimeField(blank=True, null=True)
    date_fin_validite = models.DateTimeField(blank=True, null=True)
    date_cloture = models.DateTimeField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    qty = models.FloatField()
    remise_percent = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    price_ht = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    buy_price_ht = models.FloatField(blank=True, null=True)
    fk_product_fournisseur_price = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField()
    fk_user_ouverture = models.IntegerField(blank=True, null=True)
    fk_user_cloture = models.IntegerField(blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_contratdet'


class LlxdxContratdetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_contratdet_extrafields'


class LlxdxContratdetLog(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_contratdet = models.ForeignKey(LlxdxContratdet, models.DO_NOTHING, db_column='fk_contratdet')
    date = models.DateTimeField()
    statut = models.SmallIntegerField()
    fk_user_author = models.IntegerField()
    commentaire = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_contratdet_log'


class LlxdxCronjob(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    jobtype = models.CharField(max_length=10)
    label = models.CharField(max_length=255)
    command = models.CharField(max_length=255, blank=True, null=True)
    classesname = models.CharField(max_length=255, blank=True, null=True)
    objectname = models.CharField(max_length=255, blank=True, null=True)
    methodename = models.CharField(max_length=255, blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    md5params = models.CharField(max_length=32, blank=True, null=True)
    module_name = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    datelastrun = models.DateTimeField(blank=True, null=True)
    datenextrun = models.DateTimeField(blank=True, null=True)
    datestart = models.DateTimeField(blank=True, null=True)
    dateend = models.DateTimeField(blank=True, null=True)
    datelastresult = models.DateTimeField(blank=True, null=True)
    lastresult = models.TextField(blank=True, null=True)
    lastoutput = models.TextField(blank=True, null=True)
    unitfrequency = models.CharField(max_length=255)
    frequency = models.IntegerField()
    maxrun = models.IntegerField()
    nbrun = models.IntegerField(blank=True, null=True)
    autodelete = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    test = models.CharField(max_length=255, blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_mod = models.IntegerField(blank=True, null=True)
    fk_mailing = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    libname = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)
    processing = models.IntegerField()
    email_alert = models.CharField(max_length=128, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_cronjob'
        unique_together = (('label', 'entity'),)


class LlxdxDefaultValues(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    type = models.CharField(max_length=10, blank=True, null=True)
    user_id = models.IntegerField()
    page = models.CharField(max_length=255, blank=True, null=True)
    param = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_default_values'
        unique_together = (('type', 'entity', 'user_id', 'page', 'param'),)


class LlxdxDelivery(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_int = models.CharField(max_length=30, blank=True, null=True)
    ref_customer = models.CharField(max_length=30, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    fk_user_valid = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_valid', related_name='llxdxdelivery_fk_user_valid_set', blank=True, null=True)
    date_delivery = models.DateTimeField(blank=True, null=True)
    fk_address = models.IntegerField(blank=True, null=True)
    fk_statut = models.SmallIntegerField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_delivery'
        unique_together = (('ref', 'entity'),)


class LlxdxDeliveryExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_delivery_extrafields'


class LlxdxDeliverydet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_delivery = models.ForeignKey(LlxdxDelivery, models.DO_NOTHING, db_column='fk_delivery', blank=True, null=True)
    fk_origin_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_deliverydet'


class LlxdxDeliverydetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_deliverydet_extrafields'


class LlxdxDeplacement(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30, blank=True, null=True)
    entity = models.IntegerField()
    datec = models.DateTimeField()
    tms = models.DateTimeField()
    dated = models.DateTimeField(blank=True, null=True)
    fk_user = models.IntegerField()
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=12)
    fk_statut = models.IntegerField()
    km = models.FloatField(blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_projet = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_deplacement'


class LlxdxDocumentModel(models.Model):
    rowid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    entity = models.IntegerField()
    type = models.CharField(max_length=64, blank=True, null=True)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_document_model'
        unique_together = (('nom', 'type', 'entity'),)


class LlxdxDon(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30, blank=True, null=True)
    entity = models.IntegerField()
    tms = models.DateTimeField()
    fk_statut = models.SmallIntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    datedon = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    fk_payment = models.IntegerField(blank=True, null=True)
    paid = models.SmallIntegerField()
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    societe = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zip = models.CharField(max_length=30, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    fk_country = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    phone_mobile = models.CharField(max_length=24, blank=True, null=True)
    public = models.SmallIntegerField()
    fk_projet = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField()
    fk_user_valid = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_don'
        unique_together = (('ref', 'entity'),)


class LlxdxDonExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_don_extrafields'


class LlxdxEcmDirectories(models.Model):
    rowid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=64)
    entity = models.IntegerField()
    fk_parent = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255)
    cachenbofdoc = models.IntegerField()
    fullpath = models.CharField(max_length=750, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    date_c = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_c = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_c', blank=True, null=True)
    fk_user_m = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_m', related_name='llxdxecmdirectories_fk_user_m_set', blank=True, null=True)
    acl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_ecm_directories'
        unique_together = (('label', 'fk_parent', 'entity'),)


class LlxdxEcmDirectoriesExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_ecm_directories_extrafields'


class LlxdxEcmFiles(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128, blank=True, null=True)
    label = models.CharField(max_length=128)
    share = models.CharField(max_length=128, blank=True, null=True)
    share_pass = models.CharField(max_length=32, blank=True, null=True)
    entity = models.IntegerField()
    filename = models.CharField(max_length=255)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    fullpath_orig = models.CharField(max_length=750, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    cover = models.TextField(blank=True, null=True)
    gen_or_uploaded = models.CharField(max_length=12, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    date_c = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_c = models.IntegerField(blank=True, null=True)
    fk_user_m = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=750, blank=True, null=True)
    src_object_type = models.CharField(max_length=64, blank=True, null=True)
    src_object_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_ecm_files'
        unique_together = (('filepath', 'filename', 'entity'),)


class LlxdxEcmFilesExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_ecm_files_extrafields'


class LlxdxElementCategorie(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_categorie = models.ForeignKey(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie')
    fk_element = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_element_categorie'
        unique_together = (('fk_element', 'fk_categorie'),)


class LlxdxElementContact(models.Model):
    rowid = models.AutoField(primary_key=True)
    datecreate = models.DateTimeField(blank=True, null=True)
    statut = models.SmallIntegerField(blank=True, null=True)
    element_id = models.IntegerField()
    fk_c_type_contact = models.ForeignKey(LlxdxCTypeContact, models.DO_NOTHING, db_column='fk_c_type_contact')
    fk_socpeople = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_element_contact'
        unique_together = (('element_id', 'fk_c_type_contact', 'fk_socpeople'),)


class LlxdxElementElement(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_source = models.IntegerField()
    sourcetype = models.CharField(max_length=32)
    fk_target = models.IntegerField()
    targettype = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'llxdx_element_element'
        unique_together = (('fk_source', 'sourcetype', 'fk_target', 'targettype'),)


class LlxdxElementResources(models.Model):
    rowid = models.AutoField(primary_key=True)
    element_id = models.IntegerField(blank=True, null=True)
    element_type = models.CharField(max_length=64, blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    resource_type = models.CharField(max_length=64, blank=True, null=True)
    busy = models.IntegerField(blank=True, null=True)
    mandatory = models.IntegerField(blank=True, null=True)
    duree = models.FloatField(blank=True, null=True)
    fk_user_create = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_element_resources'
        unique_together = (('resource_id', 'resource_type', 'element_id', 'element_type'),)


class LlxdxElementTag(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    lang = models.CharField(max_length=5)
    tag = models.CharField(max_length=255)
    fk_element = models.IntegerField()
    element = models.CharField(max_length=64)
    fk_categorie = models.ForeignKey(LlxdxCategorie, models.DO_NOTHING, db_column='fk_categorie', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_element_tag'
        unique_together = (('entity', 'lang', 'tag', 'fk_element', 'element'), ('fk_categorie', 'fk_element'),)


class LlxdxElementTime(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_element = models.IntegerField()
    elementtype = models.CharField(max_length=32)
    element_date = models.DateField(blank=True, null=True)
    element_datehour = models.DateTimeField(blank=True, null=True)
    element_date_withhour = models.IntegerField(blank=True, null=True)
    element_duration = models.FloatField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    thm = models.FloatField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    invoice_line_id = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    intervention_id = models.IntegerField(blank=True, null=True)
    intervention_line_id = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    ref_ext = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_element_time'


class LlxdxEmailcollectorEmailcollector(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref = models.CharField(max_length=128)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    source_directory = models.CharField(max_length=255)
    target_directory = models.CharField(max_length=255, blank=True, null=True)
    datelastresult = models.DateTimeField(blank=True, null=True)
    codelastresult = models.CharField(max_length=16, blank=True, null=True)
    lastresult = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.IntegerField()
    datelastok = models.DateTimeField(blank=True, null=True)
    maxemailpercollect = models.IntegerField(blank=True, null=True)
    hostcharset = models.CharField(max_length=16, blank=True, null=True)
    imap_encryption = models.CharField(max_length=16, blank=True, null=True)
    norsh = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    port = models.CharField(max_length=10, blank=True, null=True)
    acces_type = models.IntegerField(blank=True, null=True)
    oauth_service = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_emailcollector_emailcollector'
        unique_together = (('ref', 'entity'),)


class LlxdxEmailcollectorEmailcollectoraction(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_emailcollector = models.ForeignKey(LlxdxEmailcollectorEmailcollector, models.DO_NOTHING, db_column='fk_emailcollector')
    type = models.CharField(max_length=128)
    actionparam = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_emailcollector_emailcollectoraction'
        unique_together = (('fk_emailcollector', 'type'),)


class LlxdxEmailcollectorEmailcollectorfilter(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_emailcollector = models.ForeignKey(LlxdxEmailcollectorEmailcollector, models.DO_NOTHING, db_column='fk_emailcollector')
    type = models.CharField(max_length=128)
    rulevalue = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_emailcollector_emailcollectorfilter'
        unique_together = (('fk_emailcollector', 'type', 'rulevalue'),)


class LlxdxEntrepot(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    ref = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()
    fk_project = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lieu = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    fk_departement = models.IntegerField(blank=True, null=True)
    fk_pays = models.IntegerField(blank=True, null=True)
    statut = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_parent = models.IntegerField(blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    warehouse_usage = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=180, blank=True, null=True)
    fk_barcode_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_entrepot'
        unique_together = (('ref', 'entity'),)


class LlxdxEntrepotExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_entrepot_extrafields'


class LlxdxEstablishment(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=25, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    fk_state = models.IntegerField(blank=True, null=True)
    fk_country = models.IntegerField(blank=True, null=True)
    profid1 = models.CharField(max_length=20, blank=True, null=True)
    profid2 = models.CharField(max_length=20, blank=True, null=True)
    profid3 = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fk_user_author = models.IntegerField()
    fk_user_mod = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField()
    tms = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=30)
    label = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_establishment'


class LlxdxEventElement(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_source = models.IntegerField()
    fk_target = models.IntegerField()
    targettype = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'llxdx_event_element'


class LlxdxEventorganizationConferenceorboothattendee(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_actioncomm = models.IntegerField(blank=True, null=True)
    fk_project = models.IntegerField()
    fk_invoice = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    email_company = models.CharField(max_length=128, blank=True, null=True)
    date_subscription = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField()
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_eventorganization_conferenceorboothattendee'
        unique_together = (('fk_project', 'email', 'fk_actioncomm'),)


class LlxdxEventorganizationConferenceorboothattendeeExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_eventorganization_conferenceorboothattendee_extrafields'


class LlxdxEvents(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    type = models.CharField(max_length=32)
    entity = models.IntegerField()
    dateevent = models.DateTimeField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=250)
    ip = models.CharField(max_length=250, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    fk_object = models.IntegerField(blank=True, null=True)
    prefix_session = models.CharField(max_length=255, blank=True, null=True)
    authentication_method = models.CharField(max_length=64, blank=True, null=True)
    fk_oauth_token = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_events'


class LlxdxExpedition(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    fk_projet = models.IntegerField(blank=True, null=True)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_int = models.CharField(max_length=30, blank=True, null=True)
    ref_customer = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    fk_user_valid = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_valid', related_name='llxdxexpedition_fk_user_valid_set', blank=True, null=True)
    date_expedition = models.DateTimeField(blank=True, null=True)
    date_delivery = models.DateTimeField(blank=True, null=True)
    fk_address = models.IntegerField(blank=True, null=True)
    fk_shipping_method = models.ForeignKey(LlxdxCShipmentMode, models.DO_NOTHING, db_column='fk_shipping_method', blank=True, null=True)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    fk_statut = models.SmallIntegerField(blank=True, null=True)
    billed = models.SmallIntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    size_units = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    weight_units = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expedition'
        unique_together = (('ref', 'entity'),)


class LlxdxExpeditionExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expedition_extrafields'


class LlxdxExpeditionPackage(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_expedition = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    fk_parcel_type = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    size_units = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    weight_units = models.IntegerField(blank=True, null=True)
    dangerous_goods = models.SmallIntegerField(blank=True, null=True)
    tail_lift = models.SmallIntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expedition_package'


class LlxdxExpeditiondet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_expedition = models.ForeignKey(LlxdxExpedition, models.DO_NOTHING, db_column='fk_expedition')
    fk_origin_line = models.IntegerField(blank=True, null=True)
    fk_entrepot = models.IntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expeditiondet'


class LlxdxExpeditiondetBatch(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_expeditiondet = models.ForeignKey(LlxdxExpeditiondet, models.DO_NOTHING, db_column='fk_expeditiondet')
    eatby = models.DateField(blank=True, null=True)
    sellby = models.DateField(blank=True, null=True)
    batch = models.CharField(max_length=128, blank=True, null=True)
    qty = models.FloatField()
    fk_origin_stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_expeditiondet_batch'


class LlxdxExpeditiondetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expeditiondet_extrafields'


class LlxdxExpensereport(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=50)
    entity = models.IntegerField()
    ref_number_int = models.IntegerField(blank=True, null=True)
    ref_ext = models.IntegerField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    date_create = models.DateTimeField()
    date_valid = models.DateTimeField(blank=True, null=True)
    date_approve = models.DateTimeField(blank=True, null=True)
    date_refuse = models.DateTimeField(blank=True, null=True)
    date_cancel = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_author = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    fk_user_validator = models.IntegerField(blank=True, null=True)
    fk_user_approve = models.IntegerField(blank=True, null=True)
    fk_user_refuse = models.IntegerField(blank=True, null=True)
    fk_user_cancel = models.IntegerField(blank=True, null=True)
    fk_statut = models.IntegerField()
    fk_c_paiement = models.IntegerField(blank=True, null=True)
    paid = models.SmallIntegerField()
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    detail_refuse = models.CharField(max_length=255, blank=True, null=True)
    detail_cancel = models.CharField(max_length=255, blank=True, null=True)
    integration_compta = models.IntegerField(blank=True, null=True)
    fk_bank_account = models.IntegerField(blank=True, null=True)
    model_pdf = models.CharField(max_length=50, blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expensereport'
        unique_together = (('ref', 'entity'),)


class LlxdxExpensereportDet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_expensereport = models.IntegerField()
    docnumber = models.CharField(max_length=128, blank=True, null=True)
    fk_c_type_fees = models.IntegerField()
    fk_projet = models.IntegerField(blank=True, null=True)
    comments = models.TextField()
    product_type = models.IntegerField(blank=True, null=True)
    qty = models.FloatField()
    subprice = models.FloatField()
    value_unit = models.FloatField()
    remise_percent = models.FloatField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    total_ht = models.FloatField()
    total_tva = models.FloatField()
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField()
    date = models.DateField()
    info_bits = models.IntegerField(blank=True, null=True)
    special_code = models.IntegerField(blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    fk_facture = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_code_ventilation = models.IntegerField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    rule_warning_message = models.TextField(blank=True, null=True)
    fk_c_exp_tax_cat = models.IntegerField(blank=True, null=True)
    fk_ecm_files = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expensereport_det'


class LlxdxExpensereportExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expensereport_extrafields'


class LlxdxExpensereportIk(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_c_exp_tax_cat = models.IntegerField()
    fk_range = models.IntegerField()
    coef = models.FloatField()
    ikoffset = models.FloatField()
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expensereport_ik'


class LlxdxExpensereportRules(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    dates = models.DateTimeField()
    datee = models.DateTimeField()
    amount = models.FloatField(blank=True, null=True)
    restrictive = models.IntegerField()
    fk_user = models.IntegerField(blank=True, null=True)
    fk_usergroup = models.IntegerField(blank=True, null=True)
    fk_c_type_fees = models.IntegerField()
    code_expense_rules_type = models.CharField(max_length=50)
    is_for_all = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_expensereport_rules'


class LlxdxExportCompta(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=12)
    date_export = models.DateTimeField()
    fk_user = models.IntegerField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_export_compta'


class LlxdxExportModel(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_user = models.IntegerField()
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=64, blank=True, null=True)
    field = models.TextField()
    filter = models.TextField(blank=True, null=True)
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_export_model'
        unique_together = (('label', 'type'),)


class LlxdxExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    entity = models.IntegerField()
    elementtype = models.CharField(max_length=64)
    tms = models.DateTimeField()
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=8, blank=True, null=True)
    size = models.CharField(max_length=8, blank=True, null=True)
    fieldunique = models.IntegerField(blank=True, null=True)
    fieldrequired = models.IntegerField(blank=True, null=True)
    perms = models.CharField(max_length=255, blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)
    alwayseditable = models.IntegerField(blank=True, null=True)
    param = models.TextField(blank=True, null=True)
    list = models.CharField(max_length=128, blank=True, null=True)
    totalizable = models.IntegerField(blank=True, null=True)
    ishidden = models.IntegerField(blank=True, null=True)
    fieldcomputed = models.TextField(blank=True, null=True)
    fielddefault = models.TextField(blank=True, null=True)
    langs = models.CharField(max_length=64, blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    enabled = models.CharField(max_length=255, blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    printable = models.IntegerField(blank=True, null=True)
    css = models.CharField(max_length=128, blank=True, null=True)
    cssview = models.CharField(max_length=128, blank=True, null=True)
    csslist = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_extrafields'
        unique_together = (('name', 'entity', 'elementtype'),)


class LlxdxFacture(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_int = models.CharField(max_length=255, blank=True, null=True)
    ref_client = models.CharField(max_length=255, blank=True, null=True)
    type = models.SmallIntegerField()
    increment = models.CharField(max_length=10, blank=True, null=True)
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    datec = models.DateTimeField(blank=True, null=True)
    datef = models.DateField(blank=True, null=True)
    date_pointoftax = models.DateField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    date_closing = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    paye = models.SmallIntegerField()
    remise_percent = models.FloatField(blank=True, null=True)
    remise_absolue = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    close_code = models.CharField(max_length=16, blank=True, null=True)
    close_missing_amount = models.FloatField(blank=True, null=True)
    close_note = models.CharField(max_length=128, blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    revenuestamp = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    fk_statut = models.SmallIntegerField()
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_valid', related_name='llxdxfacture_fk_user_valid_set', blank=True, null=True)
    fk_user_closing = models.IntegerField(blank=True, null=True)
    fk_facture_source = models.ForeignKey('self', models.DO_NOTHING, db_column='fk_facture_source', blank=True, null=True)
    fk_projet = models.ForeignKey('LlxdxProjet', models.DO_NOTHING, db_column='fk_projet', blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_currency = models.CharField(max_length=3, blank=True, null=True)
    fk_cond_reglement = models.IntegerField()
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    date_lim_reglement = models.DateField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    fk_transport_mode = models.IntegerField(blank=True, null=True)
    situation_cycle_ref = models.IntegerField(blank=True, null=True)
    situation_counter = models.SmallIntegerField(blank=True, null=True)
    situation_final = models.SmallIntegerField(blank=True, null=True)
    retained_warranty = models.FloatField(blank=True, null=True)
    retained_warranty_date_limit = models.DateField(blank=True, null=True)
    retained_warranty_fk_cond_reglement = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    fk_fac_rec_source = models.IntegerField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    module_source = models.CharField(max_length=32, blank=True, null=True)
    pos_source = models.CharField(max_length=32, blank=True, null=True)
    prorata_discount = models.FloatField(blank=True, null=True)
    subtype = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture'
        unique_together = (('ref', 'entity'),)


class LlxdxFactureExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    docref001 = models.CharField(unique=True, max_length=20)
    afip001 = models.CharField(max_length=14)
    fpago001 = models.DateField(blank=True, null=True)
    dpago001 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_extrafields'


class LlxdxFactureFourn(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=255)
    ref_supplier = models.CharField(max_length=255)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    type = models.SmallIntegerField()
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    datec = models.DateTimeField(blank=True, null=True)
    datef = models.DateField(blank=True, null=True)
    tms = models.DateTimeField()
    libelle = models.CharField(max_length=255, blank=True, null=True)
    paye = models.SmallIntegerField()
    amount = models.FloatField()
    remise = models.FloatField(blank=True, null=True)
    close_code = models.CharField(max_length=16, blank=True, null=True)
    close_missing_amount = models.FloatField(blank=True, null=True)
    close_note = models.CharField(max_length=128, blank=True, null=True)
    vat_reverse_charge = models.IntegerField(blank=True, null=True)
    tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    fk_statut = models.SmallIntegerField()
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_valid', related_name='llxdxfacturefourn_fk_user_valid_set', blank=True, null=True)
    fk_user_closing = models.IntegerField(blank=True, null=True)
    fk_facture_source = models.IntegerField(blank=True, null=True)
    fk_projet = models.ForeignKey('LlxdxProjet', models.DO_NOTHING, db_column='fk_projet', blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_cond_reglement = models.IntegerField(blank=True, null=True)
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    date_lim_reglement = models.DateField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    fk_transport_mode = models.IntegerField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    date_pointoftax = models.DateField(blank=True, null=True)
    date_valid = models.DateField(blank=True, null=True)
    date_closing = models.DateTimeField(blank=True, null=True)
    fk_fac_rec_source = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn'
        unique_together = (('ref_supplier', 'fk_soc', 'entity'), ('ref', 'entity'),)


class LlxdxFactureFournDet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_facture_fourn = models.ForeignKey(LlxdxFactureFourn, models.DO_NOTHING, db_column='fk_facture_fourn')
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=128, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pu_ht = models.FloatField(blank=True, null=True)
    pu_ttc = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    fk_code_ventilation = models.IntegerField()
    special_code = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn_det'
        unique_together = (('fk_remise_except', 'fk_facture_fourn'),)


class LlxdxFactureFournDetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn_det_extrafields'


class LlxdxFactureFournDetRec(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_facture_fourn = models.IntegerField()
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=50, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pu_ht = models.FloatField(blank=True, null=True)
    pu_ttc = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    date_start = models.IntegerField(blank=True, null=True)
    date_end = models.IntegerField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    special_code = models.PositiveIntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn_det_rec'


class LlxdxFactureFournDetRecExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn_det_rec_extrafields'


class LlxdxFactureFournExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn_extrafields'


class LlxdxFactureFournRec(models.Model):
    rowid = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    ref_supplier = models.CharField(max_length=180)
    entity = models.IntegerField()
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    suspended = models.IntegerField(blank=True, null=True)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField()
    remise = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_projet = models.ForeignKey('LlxdxProjet', models.DO_NOTHING, db_column='fk_projet', blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_cond_reglement = models.IntegerField(blank=True, null=True)
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    date_lim_reglement = models.DateField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    modelpdf = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    usenewprice = models.IntegerField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    unit_frequency = models.CharField(max_length=2, blank=True, null=True)
    date_when = models.DateTimeField(blank=True, null=True)
    date_last_gen = models.DateTimeField(blank=True, null=True)
    nb_gen_done = models.IntegerField(blank=True, null=True)
    nb_gen_max = models.IntegerField(blank=True, null=True)
    auto_validate = models.IntegerField(blank=True, null=True)
    generate_pdf = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn_rec'
        unique_together = (('ref_supplier', 'fk_soc', 'entity'), ('titre', 'entity'),)


class LlxdxFactureFournRecExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_fourn_rec_extrafields'


class LlxdxFactureRec(models.Model):
    rowid = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    entity = models.IntegerField()
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    datec = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField()
    remise = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise_absolue = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    revenuestamp = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    fk_projet = models.ForeignKey('LlxdxProjet', models.DO_NOTHING, db_column='fk_projet', blank=True, null=True)
    fk_cond_reglement = models.IntegerField()
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    date_lim_reglement = models.DateField(blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    modelpdf = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    usenewprice = models.IntegerField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    unit_frequency = models.CharField(max_length=2, blank=True, null=True)
    date_when = models.DateTimeField(blank=True, null=True)
    date_last_gen = models.DateTimeField(blank=True, null=True)
    nb_gen_done = models.IntegerField(blank=True, null=True)
    nb_gen_max = models.IntegerField(blank=True, null=True)
    auto_validate = models.IntegerField(blank=True, null=True)
    generate_pdf = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_rec'
        unique_together = (('titre', 'entity'),)


class LlxdxFactureRecExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facture_rec_extrafields'


class LlxdxFacturedet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_facture = models.ForeignKey(LlxdxFacture, models.DO_NOTHING, db_column='fk_facture')
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    buy_price_ht = models.FloatField(blank=True, null=True)
    fk_product_fournisseur_price = models.IntegerField(blank=True, null=True)
    fk_code_ventilation = models.IntegerField()
    special_code = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    fk_contract_line = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    situation_percent = models.FloatField(blank=True, null=True)
    fk_prev_id = models.IntegerField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facturedet'
        unique_together = (('fk_remise_except', 'fk_facture'),)


class LlxdxFacturedetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    aaa10 = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'llxdx_facturedet_extrafields'


class LlxdxFacturedetRec(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_facture = models.IntegerField()
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    special_code = models.PositiveIntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    fk_contract_line = models.IntegerField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    date_start_fill = models.IntegerField(blank=True, null=True)
    date_end_fill = models.IntegerField(blank=True, null=True)
    buy_price_ht = models.FloatField(blank=True, null=True)
    fk_product_fournisseur_price = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facturedet_rec'


class LlxdxFacturedetRecExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_facturedet_rec_extrafields'


class LlxdxFichinter(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    fk_projet = models.IntegerField(blank=True, null=True)
    fk_contrat = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=30)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_client = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    datei = models.DateField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    fk_statut = models.SmallIntegerField(blank=True, null=True)
    dateo = models.DateField(blank=True, null=True)
    datee = models.DateField(blank=True, null=True)
    datet = models.DateField(blank=True, null=True)
    duree = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_fichinter'
        unique_together = (('ref', 'entity'),)


class LlxdxFichinterExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_fichinter_extrafields'


class LlxdxFichinterRec(models.Model):
    rowid = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50)
    entity = models.IntegerField()
    fk_soc = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    fk_contrat = models.IntegerField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    fk_projet = models.ForeignKey('LlxdxProjet', models.DO_NOTHING, db_column='fk_projet', blank=True, null=True)
    duree = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    modelpdf = models.CharField(max_length=50, blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    unit_frequency = models.CharField(max_length=2, blank=True, null=True)
    date_when = models.DateTimeField(blank=True, null=True)
    date_last_gen = models.DateTimeField(blank=True, null=True)
    nb_gen_done = models.IntegerField(blank=True, null=True)
    nb_gen_max = models.IntegerField(blank=True, null=True)
    auto_validate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_fichinter_rec'
        unique_together = (('titre', 'entity'),)


class LlxdxFichinterdet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_fichinter = models.ForeignKey(LlxdxFichinter, models.DO_NOTHING, db_column='fk_fichinter', blank=True, null=True)
    fk_parent_line = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_fichinterdet'


class LlxdxFichinterdetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_fichinterdet_extrafields'


class LlxdxFichinterdetRec(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_fichinter = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=1, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=1, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    buy_price_ht = models.FloatField(blank=True, null=True)
    fk_product_fournisseur_price = models.IntegerField(blank=True, null=True)
    fk_code_ventilation = models.IntegerField()
    special_code = models.PositiveIntegerField(blank=True, null=True)
    fk_unit = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_fichinterdet_rec'


class LlxdxHoliday(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_user = models.IntegerField()
    fk_user_create = models.IntegerField(blank=True, null=True)
    fk_type = models.IntegerField()
    date_create = models.DateTimeField()
    description = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    halfday = models.IntegerField(blank=True, null=True)
    statut = models.IntegerField()
    fk_validator = models.IntegerField()
    date_valid = models.DateTimeField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    date_refuse = models.DateTimeField(blank=True, null=True)
    fk_user_refuse = models.IntegerField(blank=True, null=True)
    date_cancel = models.DateTimeField(blank=True, null=True)
    fk_user_cancel = models.IntegerField(blank=True, null=True)
    detail_refuse = models.CharField(max_length=250, blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    tms = models.DateTimeField()
    ref = models.CharField(max_length=30)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    date_approval = models.DateTimeField(blank=True, null=True)
    fk_user_approve = models.IntegerField(blank=True, null=True)
    nb_open_day = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_holiday'


class LlxdxHolidayConfig(models.Model):
    rowid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_holiday_config'


class LlxdxHolidayExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_holiday_extrafields'


class LlxdxHolidayLogs(models.Model):
    rowid = models.AutoField(primary_key=True)
    date_action = models.DateTimeField()
    fk_user_action = models.IntegerField()
    fk_user_update = models.IntegerField()
    fk_type = models.IntegerField()
    type_action = models.CharField(max_length=255)
    prev_solde = models.CharField(max_length=255)
    new_solde = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'llxdx_holiday_logs'


class LlxdxHolidayUsers(models.Model):
    fk_user = models.IntegerField()
    fk_type = models.IntegerField()
    nb_holiday = models.FloatField()

    class Meta:
        managed = False
        db_table = 'llxdx_holiday_users'
        unique_together = (('fk_user', 'fk_type'),)


class LlxdxHrmEvaluation(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.SmallIntegerField()
    date_eval = models.DateField(blank=True, null=True)
    fk_user = models.IntegerField()
    fk_job = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_evaluation'


class LlxdxHrmEvaluationExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_evaluation_extrafields'


class LlxdxHrmEvaluationdet(models.Model):
    rowid = models.AutoField(primary_key=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_skill = models.IntegerField()
    fk_evaluation = models.IntegerField()
    rankorder = models.IntegerField()
    required_rank = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_evaluationdet'


class LlxdxHrmEvaluationdetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_evaluationdet_extrafields'


class LlxdxHrmJob(models.Model):
    rowid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    deplacement = models.CharField(max_length=255, blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_job'


class LlxdxHrmJobExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_job_extrafields'


class LlxdxHrmJobUser(models.Model):
    rowid = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_contrat = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    fk_job = models.IntegerField()
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    abort_comment = models.CharField(max_length=255, blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_job_user'


class LlxdxHrmSkill(models.Model):
    rowid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    required_level = models.IntegerField()
    date_validite = models.IntegerField()
    temps_theorique = models.FloatField()
    skill_type = models.IntegerField()
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_skill'


class LlxdxHrmSkillExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_skill_extrafields'


class LlxdxHrmSkilldet(models.Model):
    rowid = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_skill = models.IntegerField()
    rankorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_skilldet'


class LlxdxHrmSkillrank(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_skill = models.IntegerField()
    rankorder = models.IntegerField()
    fk_object = models.IntegerField()
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    objecttype = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'llxdx_hrm_skillrank'


class LlxdxImportModel(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_user = models.IntegerField()
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=64, blank=True, null=True)
    field = models.TextField()
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_import_model'
        unique_together = (('label', 'type'),)


class LlxdxIntracommreport(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    type_declaration = models.CharField(max_length=32, blank=True, null=True)
    periods = models.CharField(max_length=32, blank=True, null=True)
    mode = models.CharField(max_length=32, blank=True, null=True)
    content_xml = models.TextField(blank=True, null=True)
    type_export = models.CharField(max_length=10, blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_intracommreport'


class LlxdxInventory(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=48, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    fk_warehouse = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    date_inventory = models.DateTimeField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    date_validation = models.DateTimeField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    categories_product = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_inventory'
        unique_together = (('ref', 'entity'),)


class LlxdxInventoryExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_inventory_extrafields'


class LlxdxInventorydet(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_inventory = models.IntegerField(blank=True, null=True)
    fk_warehouse = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    batch = models.CharField(max_length=30, blank=True, null=True)
    qty_view = models.FloatField(blank=True, null=True)
    qty_stock = models.FloatField(blank=True, null=True)
    qty_regulated = models.FloatField(blank=True, null=True)
    fk_movement = models.IntegerField(blank=True, null=True)
    pmp_real = models.FloatField(blank=True, null=True)
    pmp_expected = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_inventorydet'
        unique_together = (('fk_inventory', 'fk_warehouse', 'fk_product', 'batch'),)


class LlxdxKnowledgemanagementKnowledgerecord(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    fk_user_creat = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    fk_ticket = models.IntegerField(blank=True, null=True)
    fk_c_ticket_category = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    lang = models.CharField(max_length=6, blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_knowledgemanagement_knowledgerecord'


class LlxdxKnowledgemanagementKnowledgerecordExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_knowledgemanagement_knowledgerecord_extrafields'


class LlxdxLinks(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    datea = models.DateTimeField()
    url = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    objecttype = models.CharField(max_length=255)
    objectid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_links'
        unique_together = (('objectid', 'label'),)


class LlxdxLoan(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    label = models.CharField(max_length=80)
    fk_bank = models.IntegerField(blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    datestart = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    nbterm = models.FloatField(blank=True, null=True)
    rate = models.FloatField()
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    capital_position = models.FloatField(blank=True, null=True)
    date_position = models.DateField(blank=True, null=True)
    paid = models.SmallIntegerField()
    accountancy_account_capital = models.CharField(max_length=32, blank=True, null=True)
    accountancy_account_insurance = models.CharField(max_length=32, blank=True, null=True)
    accountancy_account_interest = models.CharField(max_length=32, blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    fk_projet = models.IntegerField(blank=True, null=True)
    insurance_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_loan'


class LlxdxLoanSchedule(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_loan = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateTimeField(blank=True, null=True)
    amount_capital = models.FloatField(blank=True, null=True)
    amount_insurance = models.FloatField(blank=True, null=True)
    amount_interest = models.FloatField(blank=True, null=True)
    fk_typepayment = models.IntegerField()
    num_payment = models.CharField(max_length=50, blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_payment_loan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_loan_schedule'
        unique_together = (('fk_loan', 'datep'),)


class LlxdxLocaltax(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    localtaxtype = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateField(blank=True, null=True)
    datev = models.DateField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_localtax'


class LlxdxMailing(models.Model):
    rowid = models.AutoField(primary_key=True)
    statut = models.SmallIntegerField(blank=True, null=True)
    titre = models.CharField(max_length=128, blank=True, null=True)
    entity = models.IntegerField()
    sujet = models.CharField(max_length=128, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    bgcolor = models.CharField(max_length=8, blank=True, null=True)
    bgimage = models.CharField(max_length=255, blank=True, null=True)
    cible = models.CharField(max_length=60, blank=True, null=True)
    nbemail = models.IntegerField(blank=True, null=True)
    email_from = models.CharField(max_length=160, blank=True, null=True)
    name_from = models.CharField(max_length=128, blank=True, null=True)
    email_replyto = models.CharField(max_length=160, blank=True, null=True)
    email_errorsto = models.CharField(max_length=160, blank=True, null=True)
    tag = models.CharField(max_length=128, blank=True, null=True)
    date_creat = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    date_appro = models.DateTimeField(blank=True, null=True)
    date_envoi = models.DateTimeField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    fk_user_appro = models.IntegerField(blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    joined_file1 = models.CharField(max_length=255, blank=True, null=True)
    joined_file2 = models.CharField(max_length=255, blank=True, null=True)
    joined_file3 = models.CharField(max_length=255, blank=True, null=True)
    joined_file4 = models.CharField(max_length=255, blank=True, null=True)
    tms = models.DateTimeField()
    evenunsubscribe = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_mailing'
        unique_together = (('titre', 'entity'),)


class LlxdxMailingAdvtarget(models.Model):
    rowid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    entity = models.IntegerField()
    filtervalue = models.TextField(blank=True, null=True)
    fk_user_author = models.IntegerField()
    datec = models.DateTimeField()
    fk_user_mod = models.IntegerField()
    tms = models.DateTimeField()
    fk_element = models.IntegerField()
    type_element = models.CharField(max_length=180)

    class Meta:
        managed = False
        db_table = 'llxdx_mailing_advtarget'


class LlxdxMailingCibles(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_mailing = models.IntegerField()
    fk_contact = models.IntegerField()
    lastname = models.CharField(max_length=160, blank=True, null=True)
    firstname = models.CharField(max_length=160, blank=True, null=True)
    email = models.CharField(max_length=160)
    other = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=64, blank=True, null=True)
    statut = models.SmallIntegerField()
    source_url = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=32, blank=True, null=True)
    date_envoi = models.DateTimeField(blank=True, null=True)
    error_text = models.CharField(max_length=255, blank=True, null=True)
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_mailing_cibles'
        unique_together = (('fk_mailing', 'email'),)


class LlxdxMailingUnsubscribe(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    unsubscribegroup = models.CharField(max_length=128, blank=True, null=True)
    ip = models.CharField(max_length=128, blank=True, null=True)
    date_creat = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_mailing_unsubscribe'
        unique_together = (('email', 'entity', 'unsubscribegroup'),)


class LlxdxMenu(models.Model):
    rowid = models.AutoField(primary_key=True)
    menu_handler = models.CharField(max_length=16)
    entity = models.IntegerField()
    module = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=4)
    mainmenu = models.CharField(max_length=100)
    leftmenu = models.CharField(max_length=100, blank=True, null=True)
    fk_menu = models.IntegerField()
    fk_mainmenu = models.CharField(max_length=100, blank=True, null=True)
    fk_leftmenu = models.CharField(max_length=100, blank=True, null=True)
    position = models.IntegerField()
    url = models.CharField(max_length=255)
    target = models.CharField(max_length=100, blank=True, null=True)
    titre = models.CharField(max_length=255)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    langs = models.CharField(max_length=100, blank=True, null=True)
    level = models.SmallIntegerField(blank=True, null=True)
    perms = models.TextField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)
    usertype = models.IntegerField()
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_menu'
        unique_together = (('menu_handler', 'fk_menu', 'position', 'url', 'entity'),)


class LlxdxMrpMo(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    entity = models.IntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    qty = models.FloatField()
    fk_warehouse = models.IntegerField(blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    date_valid = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.IntegerField()
    fk_product = models.IntegerField()
    date_start_planned = models.DateTimeField(blank=True, null=True)
    date_end_planned = models.DateTimeField(blank=True, null=True)
    fk_bom = models.IntegerField(blank=True, null=True)
    fk_project = models.IntegerField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    mrptype = models.IntegerField(blank=True, null=True)
    fk_parent_line = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_mrp_mo'


class LlxdxMrpMoExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_mrp_mo_extrafields'


class LlxdxMrpProduction(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_mo = models.ForeignKey(LlxdxMrpMo, models.DO_NOTHING, db_column='fk_mo')
    origin_id = models.IntegerField(blank=True, null=True)
    origin_type = models.CharField(max_length=10, blank=True, null=True)
    position = models.IntegerField()
    fk_product = models.ForeignKey('LlxdxProduct', models.DO_NOTHING, db_column='fk_product')
    fk_warehouse = models.IntegerField(blank=True, null=True)
    qty = models.FloatField()
    qty_frozen = models.SmallIntegerField(blank=True, null=True)
    disable_stock_change = models.SmallIntegerField(blank=True, null=True)
    batch = models.CharField(max_length=128, blank=True, null=True)
    role = models.CharField(max_length=10, blank=True, null=True)
    fk_mrp_production = models.IntegerField(blank=True, null=True)
    fk_stock_movement = models.ForeignKey('LlxdxStockMouvement', models.DO_NOTHING, db_column='fk_stock_movement', blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_default_workstation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_mrp_production'


class LlxdxMulticurrency(models.Model):
    rowid = models.AutoField(primary_key=True)
    date_create = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_multicurrency'


class LlxdxMulticurrencyRate(models.Model):
    rowid = models.AutoField(primary_key=True)
    date_sync = models.DateTimeField(blank=True, null=True)
    rate = models.FloatField()
    fk_multicurrency = models.IntegerField()
    entity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_multicurrency_rate'


class LlxdxNotify(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    daten = models.DateTimeField(blank=True, null=True)
    fk_action = models.IntegerField()
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_contact = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    objet_type = models.CharField(max_length=24)
    objet_id = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    type_target = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_notify'


class LlxdxNotifyDef(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    datec = models.DateField(blank=True, null=True)
    fk_action = models.IntegerField()
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_contact = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    threshold = models.FloatField(blank=True, null=True)
    context = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_notify_def'


class LlxdxNotifyDefObject(models.Model):
    entity = models.IntegerField()
    objet_type = models.CharField(max_length=16, blank=True, null=True)
    objet_id = models.IntegerField()
    type_notif = models.CharField(max_length=16, blank=True, null=True)
    date_notif = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    moreparam = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_notify_def_object'


class LlxdxOauthState(models.Model):
    rowid = models.AutoField(primary_key=True)
    service = models.CharField(max_length=36, blank=True, null=True)
    state = models.CharField(max_length=128, blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    fk_adherent = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_oauth_state'


class LlxdxOauthToken(models.Model):
    rowid = models.AutoField(primary_key=True)
    service = models.CharField(max_length=36, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    fk_adherent = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)
    tokenstring = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    restricted_ips = models.CharField(max_length=200, blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_oauth_token'


class LlxdxObjectLang(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_object = models.IntegerField()
    type_object = models.CharField(max_length=32)
    property = models.CharField(max_length=32)
    lang = models.CharField(max_length=5)
    value = models.TextField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_object_lang'
        unique_together = (('fk_object', 'type_object', 'property', 'lang'),)


class LlxdxOnlinesignature(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    object_type = models.CharField(max_length=32)
    object_id = models.IntegerField()
    datec = models.DateTimeField()
    tms = models.DateTimeField()
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=128, blank=True, null=True)
    pathoffile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_onlinesignature'


class LlxdxOpensurveyComments(models.Model):
    id_comment = models.AutoField(primary_key=True)
    id_sondage = models.CharField(max_length=16)
    comment = models.TextField()
    tms = models.DateTimeField()
    usercomment = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_opensurvey_comments'


class LlxdxOpensurveyFormquestions(models.Model):
    rowid = models.AutoField(primary_key=True)
    id_sondage = models.CharField(max_length=16, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    available_answers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_opensurvey_formquestions'


class LlxdxOpensurveySondage(models.Model):
    id_sondage = models.CharField(primary_key=True, max_length=16)
    entity = models.IntegerField()
    commentaires = models.TextField(blank=True, null=True)
    mail_admin = models.CharField(max_length=128, blank=True, null=True)
    nom_admin = models.CharField(max_length=64, blank=True, null=True)
    fk_user_creat = models.IntegerField()
    titre = models.TextField()
    date_fin = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    format = models.CharField(max_length=2)
    mailsonde = models.IntegerField()
    allow_comments = models.IntegerField()
    allow_spy = models.IntegerField()
    tms = models.DateTimeField()
    sujet = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_opensurvey_sondage'


class LlxdxOpensurveyUserFormanswers(models.Model):
    fk_user_survey = models.IntegerField()
    fk_question = models.IntegerField()
    reponses = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_opensurvey_user_formanswers'


class LlxdxOpensurveyUserStuds(models.Model):
    id_users = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=64)
    id_sondage = models.CharField(max_length=16)
    reponses = models.CharField(max_length=200)
    tms = models.DateTimeField()
    ip = models.CharField(max_length=250, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_opensurvey_user_studs'


class LlxdxOverwriteTrans(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    lang = models.CharField(max_length=5, blank=True, null=True)
    transkey = models.CharField(max_length=128, blank=True, null=True)
    transvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_overwrite_trans'
        unique_together = (('entity', 'lang', 'transkey'),)


class LlxdxPaiement(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    multicurrency_amount = models.FloatField(blank=True, null=True)
    fk_paiement = models.IntegerField()
    num_paiement = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    statut = models.SmallIntegerField()
    fk_export_compta = models.IntegerField()
    pos_change = models.FloatField(blank=True, null=True)
    ext_payment_id = models.CharField(max_length=255, blank=True, null=True)
    ext_payment_site = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_paiement'


class LlxdxPaiementFacture(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_paiement = models.ForeignKey(LlxdxPaiement, models.DO_NOTHING, db_column='fk_paiement', blank=True, null=True)
    fk_facture = models.ForeignKey(LlxdxFacture, models.DO_NOTHING, db_column='fk_facture', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_paiement_facture'
        unique_together = (('fk_paiement', 'fk_facture'),)


class LlxdxPaiementcharge(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_charge = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    fk_typepaiement = models.IntegerField()
    num_paiement = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_paiementcharge'


class LlxdxPaiementfourn(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30, blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    datep = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    multicurrency_amount = models.FloatField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_paiement = models.IntegerField()
    num_paiement = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField()
    statut = models.SmallIntegerField()
    model_pdf = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_paiementfourn'


class LlxdxPaiementfournFacturefourn(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_paiementfourn = models.IntegerField(blank=True, null=True)
    fk_facturefourn = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_paiementfourn_facturefourn'
        unique_together = (('fk_paiementfourn', 'fk_facturefourn'),)


class LlxdxPartnership(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    status = models.SmallIntegerField()
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_member = models.IntegerField(blank=True, null=True)
    email_partnership = models.CharField(max_length=64, blank=True, null=True)
    date_partnership_start = models.DateField()
    date_partnership_end = models.DateField(blank=True, null=True)
    entity = models.IntegerField()
    reason_decline_or_cancel = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    count_last_url_check_error = models.IntegerField(blank=True, null=True)
    last_check_backlink = models.DateTimeField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    fk_type = models.IntegerField()
    url_to_check = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_partnership'
        unique_together = (('fk_type', 'fk_soc', 'date_partnership_start'), ('fk_type', 'fk_member', 'date_partnership_start'),)


class LlxdxPartnershipExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_partnership_extrafields'


class LlxdxPaymentDonation(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_donation = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    fk_typepayment = models.IntegerField()
    num_payment = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    ext_payment_id = models.CharField(max_length=255, blank=True, null=True)
    ext_payment_site = models.CharField(max_length=128, blank=True, null=True)
    fk_bank = models.IntegerField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_payment_donation'


class LlxdxPaymentExpensereport(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_expensereport = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    fk_typepayment = models.IntegerField()
    num_payment = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_payment_expensereport'


class LlxdxPaymentLoan(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_loan = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateTimeField(blank=True, null=True)
    amount_capital = models.FloatField(blank=True, null=True)
    amount_insurance = models.FloatField(blank=True, null=True)
    amount_interest = models.FloatField(blank=True, null=True)
    fk_typepayment = models.IntegerField()
    num_payment = models.CharField(max_length=50, blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_payment_loan'


class LlxdxPaymentSalary(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30, blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    fk_user = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user', blank=True, null=True)
    datep = models.DateTimeField(blank=True, null=True)
    datev = models.DateField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    fk_projet = models.IntegerField(blank=True, null=True)
    fk_typepayment = models.IntegerField()
    num_payment = models.CharField(max_length=50, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    datesp = models.DateField(blank=True, null=True)
    dateep = models.DateField(blank=True, null=True)
    entity = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_payment_salary'


class LlxdxPaymentVarious(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30, blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    datep = models.DateField(blank=True, null=True)
    datev = models.DateField(blank=True, null=True)
    sens = models.SmallIntegerField()
    amount = models.FloatField()
    fk_typepayment = models.IntegerField()
    num_payment = models.CharField(max_length=50, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    accountancy_code = models.CharField(max_length=32, blank=True, null=True)
    fk_projet = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    subledger_account = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_payment_various'


class LlxdxPaymentVat(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_tva = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    datep = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    fk_typepaiement = models.IntegerField()
    num_paiement = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_payment_vat'


class LlxdxPosCashFence(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref = models.CharField(max_length=64, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    opening = models.FloatField(blank=True, null=True)
    cash = models.FloatField(blank=True, null=True)
    card = models.FloatField(blank=True, null=True)
    cheque = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField()
    date_valid = models.DateTimeField(blank=True, null=True)
    day_close = models.IntegerField(blank=True, null=True)
    month_close = models.IntegerField(blank=True, null=True)
    year_close = models.IntegerField(blank=True, null=True)
    posmodule = models.CharField(max_length=30, blank=True, null=True)
    posnumber = models.CharField(max_length=30, blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_pos_cash_fence'


class LlxdxPrelevement(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_facture = models.IntegerField(blank=True, null=True)
    fk_prelevement_lignes = models.ForeignKey('LlxdxPrelevementLignes', models.DO_NOTHING, db_column='fk_prelevement_lignes')
    fk_facture_fourn = models.IntegerField(blank=True, null=True)
    fk_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_prelevement'


class LlxdxPrelevementBons(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=12, blank=True, null=True)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    statut = models.SmallIntegerField(blank=True, null=True)
    credite = models.SmallIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    date_trans = models.DateTimeField(blank=True, null=True)
    method_trans = models.SmallIntegerField(blank=True, null=True)
    fk_user_trans = models.IntegerField(blank=True, null=True)
    date_credit = models.DateTimeField(blank=True, null=True)
    fk_user_credit = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    fk_bank_account = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_prelevement_bons'
        unique_together = (('ref', 'entity'),)


class LlxdxPrelevementDemande(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_facture = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    date_demande = models.DateTimeField()
    traite = models.SmallIntegerField(blank=True, null=True)
    date_traite = models.DateTimeField(blank=True, null=True)
    fk_prelevement_bons = models.IntegerField(blank=True, null=True)
    fk_user_demande = models.IntegerField()
    code_banque = models.CharField(max_length=128, blank=True, null=True)
    code_guichet = models.CharField(max_length=6, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    cle_rib = models.CharField(max_length=5, blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)
    sourcetype = models.CharField(max_length=32, blank=True, null=True)
    ext_payment_id = models.CharField(max_length=255, blank=True, null=True)
    ext_payment_site = models.CharField(max_length=128, blank=True, null=True)
    fk_facture_fourn = models.IntegerField(blank=True, null=True)
    fk_salary = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_prelevement_demande'


class LlxdxPrelevementLignes(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_prelevement_bons = models.ForeignKey(LlxdxPrelevementBons, models.DO_NOTHING, db_column='fk_prelevement_bons', blank=True, null=True)
    fk_soc = models.IntegerField()
    statut = models.SmallIntegerField(blank=True, null=True)
    client_nom = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    code_banque = models.CharField(max_length=128, blank=True, null=True)
    code_guichet = models.CharField(max_length=6, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    cle_rib = models.CharField(max_length=5, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_prelevement_lignes'


class LlxdxPrelevementRejet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_prelevement_lignes = models.IntegerField(blank=True, null=True)
    date_rejet = models.DateTimeField(blank=True, null=True)
    motif = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    fk_user_creation = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    afacturer = models.IntegerField(blank=True, null=True)
    fk_facture = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_prelevement_rejet'


class LlxdxPrinting(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    printer_name = models.TextField()
    printer_location = models.TextField()
    printer_id = models.CharField(max_length=255)
    copy = models.IntegerField()
    module = models.CharField(max_length=16)
    driver = models.CharField(max_length=16)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_printing'


class LlxdxProduct(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=128, blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_parent = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    customcode = models.CharField(max_length=32, blank=True, null=True)
    fk_country = models.ForeignKey(LlxdxCCountry, models.DO_NOTHING, db_column='fk_country', blank=True, null=True)
    fk_state = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_ttc = models.FloatField(blank=True, null=True)
    price_min = models.FloatField(blank=True, null=True)
    price_min_ttc = models.FloatField(blank=True, null=True)
    price_base_type = models.CharField(max_length=3, blank=True, null=True)
    cost_price = models.FloatField(blank=True, null=True)
    default_vat_code = models.CharField(max_length=10, blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    recuperableonly = models.IntegerField()
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    tosell = models.IntegerField(blank=True, null=True)
    tobuy = models.IntegerField(blank=True, null=True)
    onportal = models.IntegerField(blank=True, null=True)
    tobatch = models.IntegerField()
    sell_or_eat_by_mandatory = models.IntegerField()
    fk_product_type = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=6, blank=True, null=True)
    seuil_stock_alerte = models.FloatField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    fk_barcode_type = models.ForeignKey(LlxdxCBarcodeType, models.DO_NOTHING, db_column='fk_barcode_type', blank=True, null=True)
    accountancy_code_sell = models.CharField(max_length=32, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    accountancy_code_sell_intra = models.CharField(max_length=32, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    accountancy_code_sell_export = models.CharField(max_length=32, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    accountancy_code_buy = models.CharField(max_length=32, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    accountancy_code_buy_intra = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy_export = models.CharField(max_length=32, blank=True, null=True)
    partnumber = models.CharField(max_length=32, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    weight_units = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    length_units = models.IntegerField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    width_units = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    height_units = models.IntegerField(blank=True, null=True)
    surface = models.FloatField(blank=True, null=True)
    surface_units = models.IntegerField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_units = models.IntegerField(blank=True, null=True)
    stock = models.FloatField(blank=True, null=True)
    pmp = models.FloatField()
    fifo = models.FloatField(blank=True, null=True)
    lifo = models.FloatField(blank=True, null=True)
    canvas = models.CharField(max_length=32, blank=True, null=True)
    finished = models.ForeignKey(LlxdxCProductNature, models.DO_NOTHING, db_column='finished', to_field='code', blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    fk_price_expression = models.IntegerField(blank=True, null=True)
    desiredstock = models.FloatField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    price_autogen = models.IntegerField(blank=True, null=True)
    fk_default_warehouse = models.ForeignKey(LlxdxEntrepot, models.DO_NOTHING, db_column='fk_default_warehouse', blank=True, null=True)
    fk_project = models.IntegerField(blank=True, null=True)
    net_measure = models.FloatField(blank=True, null=True)
    net_measure_units = models.IntegerField(blank=True, null=True)
    batch_mask = models.CharField(max_length=32, blank=True, null=True)
    lifetime = models.IntegerField(blank=True, null=True)
    qc_frequency = models.IntegerField(blank=True, null=True)
    mandatory_period = models.IntegerField(blank=True, null=True)
    fk_default_bom = models.IntegerField(blank=True, null=True)
    fk_default_workstation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product'
        unique_together = (('ref', 'entity'), ('barcode', 'fk_barcode_type', 'entity'),)


class LlxdxProductAssociation(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product_pere = models.IntegerField()
    fk_product_fils = models.IntegerField()
    qty = models.FloatField(blank=True, null=True)
    incdec = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_association'
        unique_together = (('fk_product_pere', 'fk_product_fils'),)


class LlxdxProductAttribute(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(unique=True, max_length=255)
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255)
    position = models.IntegerField()
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_product_attribute'


class LlxdxProductAttributeCombination(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product_parent = models.IntegerField()
    fk_product_child = models.IntegerField()
    variation_price = models.FloatField()
    variation_price_percentage = models.IntegerField(blank=True, null=True)
    variation_weight = models.FloatField()
    variation_ref_ext = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_product_attribute_combination'


class LlxdxProductAttributeCombination2Val(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_prod_combination = models.IntegerField()
    fk_prod_attr = models.IntegerField()
    fk_prod_attr_val = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_product_attribute_combination2val'


class LlxdxProductAttributeCombinationPriceLevel(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product_attribute_combination = models.IntegerField()
    fk_price_level = models.IntegerField()
    variation_price = models.FloatField()
    variation_price_percentage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_attribute_combination_price_level'
        unique_together = (('fk_product_attribute_combination', 'fk_price_level'),)


class LlxdxProductAttributeValue(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product_attribute = models.IntegerField()
    ref = models.CharField(max_length=180)
    value = models.CharField(max_length=255)
    entity = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_product_attribute_value'
        unique_together = (('fk_product_attribute', 'ref'),)


class LlxdxProductBatch(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_product_stock = models.ForeignKey('LlxdxProductStock', models.DO_NOTHING, db_column='fk_product_stock')
    eatby = models.DateTimeField(blank=True, null=True)
    sellby = models.DateTimeField(blank=True, null=True)
    batch = models.CharField(max_length=128, blank=True, null=True)
    qty = models.FloatField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_batch'
        unique_together = (('fk_product_stock', 'batch'),)


class LlxdxProductCustomerPrice(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_product = models.ForeignKey(LlxdxProduct, models.DO_NOTHING, db_column='fk_product')
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc')
    price = models.FloatField(blank=True, null=True)
    price_ttc = models.FloatField(blank=True, null=True)
    price_min = models.FloatField(blank=True, null=True)
    price_min_ttc = models.FloatField(blank=True, null=True)
    price_base_type = models.CharField(max_length=3, blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    default_vat_code = models.CharField(max_length=10, blank=True, null=True)
    recuperableonly = models.IntegerField()
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10)
    fk_user = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user', blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    ref_customer = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_customer_price'
        unique_together = (('fk_product', 'fk_soc'),)


class LlxdxProductCustomerPriceLog(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    fk_product = models.IntegerField()
    fk_soc = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    price_ttc = models.FloatField(blank=True, null=True)
    price_min = models.FloatField(blank=True, null=True)
    price_min_ttc = models.FloatField(blank=True, null=True)
    price_base_type = models.CharField(max_length=3, blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    recuperableonly = models.IntegerField()
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10)
    fk_user = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    default_vat_code = models.CharField(max_length=10, blank=True, null=True)
    ref_customer = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_customer_price_log'


class LlxdxProductExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_extrafields'


class LlxdxProductFournisseurPrice(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_product = models.ForeignKey(LlxdxProduct, models.DO_NOTHING, db_column='fk_product', blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    ref_fourn = models.CharField(max_length=128, blank=True, null=True)
    desc_fourn = models.TextField(blank=True, null=True)
    fk_availability = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField()
    remise = models.FloatField()
    unitprice = models.FloatField(blank=True, null=True)
    charges = models.FloatField(blank=True, null=True)
    tva_tx = models.FloatField()
    default_vat_code = models.CharField(max_length=10, blank=True, null=True)
    info_bits = models.IntegerField()
    fk_user = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user', blank=True, null=True)
    fk_supplier_price_expression = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    delivery_time_days = models.IntegerField(blank=True, null=True)
    supplier_reputation = models.CharField(max_length=10, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_unitprice = models.FloatField(blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_price = models.FloatField(blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10)
    barcode = models.CharField(max_length=180, blank=True, null=True)
    fk_barcode_type = models.ForeignKey(LlxdxCBarcodeType, models.DO_NOTHING, db_column='fk_barcode_type', blank=True, null=True)
    packaging = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_fournisseur_price'
        unique_together = (('barcode', 'fk_barcode_type', 'entity'), ('ref_fourn', 'fk_soc', 'quantity', 'entity'),)


class LlxdxProductFournisseurPriceExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_fournisseur_price_extrafields'


class LlxdxProductFournisseurPriceLog(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    fk_product_fournisseur = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_price = models.FloatField(blank=True, null=True)
    multicurrency_unitprice = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_fournisseur_price_log'


class LlxdxProductLang(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product = models.ForeignKey(LlxdxProduct, models.DO_NOTHING, db_column='fk_product')
    lang = models.CharField(max_length=5)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_lang'
        unique_together = (('fk_product', 'lang'),)


class LlxdxProductLot(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField()
    batch = models.CharField(max_length=128, blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    eatby = models.DateField(blank=True, null=True)
    sellby = models.DateField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.IntegerField(blank=True, null=True)
    eol_date = models.DateTimeField(blank=True, null=True)
    manufacturing_date = models.DateTimeField(blank=True, null=True)
    scrapping_date = models.DateTimeField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=180, blank=True, null=True)
    fk_barcode_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_lot'
        unique_together = (('fk_product', 'batch'),)


class LlxdxProductLotExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_lot_extrafields'


class LlxdxProductPerentity(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField()
    accountancy_code_sell = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_sell_intra = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_sell_export = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy_intra = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy_export = models.CharField(max_length=32, blank=True, null=True)
    pmp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_perentity'
        unique_together = (('fk_product', 'entity'),)


class LlxdxProductPrice(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    tms = models.DateTimeField()
    fk_product = models.ForeignKey(LlxdxProduct, models.DO_NOTHING, db_column='fk_product')
    date_price = models.DateTimeField(blank=True, null=True)
    price_level = models.SmallIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_ttc = models.FloatField(blank=True, null=True)
    price_min = models.FloatField(blank=True, null=True)
    price_min_ttc = models.FloatField(blank=True, null=True)
    price_base_type = models.CharField(max_length=3, blank=True, null=True)
    tva_tx = models.FloatField()
    default_vat_code = models.CharField(max_length=10, blank=True, null=True)
    recuperableonly = models.IntegerField()
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    tosell = models.IntegerField(blank=True, null=True)
    price_by_qty = models.IntegerField()
    fk_price_expression = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_price = models.FloatField(blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_price_ttc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_price'


class LlxdxProductPriceByQty(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product_price = models.ForeignKey(LlxdxProductPrice, models.DO_NOTHING, db_column='fk_product_price')
    price = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField()
    remise = models.FloatField()
    unitprice = models.FloatField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    price_base_type = models.CharField(max_length=3, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_price = models.FloatField(blank=True, null=True)
    multicurrency_price_ttc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_price_by_qty'
        unique_together = (('fk_product_price', 'quantity'),)


class LlxdxProductPricerules(models.Model):
    rowid = models.AutoField(primary_key=True)
    level = models.IntegerField(unique=True)
    fk_level = models.IntegerField()
    var_percent = models.FloatField()
    var_min_percent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'llxdx_product_pricerules'


class LlxdxProductStock(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_product = models.ForeignKey(LlxdxProduct, models.DO_NOTHING, db_column='fk_product')
    fk_entrepot = models.ForeignKey(LlxdxEntrepot, models.DO_NOTHING, db_column='fk_entrepot')
    reel = models.FloatField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_stock'
        unique_together = (('fk_product', 'fk_entrepot'),)


class LlxdxProductWarehouseProperties(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_product = models.IntegerField()
    fk_entrepot = models.IntegerField()
    seuil_stock_alerte = models.FloatField(blank=True, null=True)
    desiredstock = models.FloatField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_product_warehouse_properties'


class LlxdxProjet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc', blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    dateo = models.DateField(blank=True, null=True)
    datee = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=50, blank=True, null=True)
    entity = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    fk_user_creat = models.IntegerField()
    public = models.IntegerField(blank=True, null=True)
    fk_statut = models.IntegerField()
    fk_opp_status = models.IntegerField(blank=True, null=True)
    opp_percent = models.FloatField(blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    fk_user_close = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    opp_amount = models.FloatField(blank=True, null=True)
    budget_amount = models.FloatField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    usage_bill_time = models.IntegerField(blank=True, null=True)
    usage_opportunity = models.IntegerField(blank=True, null=True)
    usage_task = models.IntegerField(blank=True, null=True)
    usage_organize_event = models.IntegerField(blank=True, null=True)
    email_msgid = models.CharField(max_length=255, blank=True, null=True)
    fk_opp_status_end = models.IntegerField(blank=True, null=True)
    accept_conference_suggestions = models.IntegerField(blank=True, null=True)
    accept_booth_suggestions = models.IntegerField(blank=True, null=True)
    price_registration = models.FloatField(blank=True, null=True)
    price_booth = models.FloatField(blank=True, null=True)
    max_attendees = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)
    date_start_event = models.DateTimeField(blank=True, null=True)
    date_end_event = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_project = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_projet'
        unique_together = (('ref', 'entity'),)


class LlxdxProjetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    f001 = models.DateField(blank=True, null=True)
    rev1 = models.IntegerField(blank=True, null=True)
    resp1 = models.CharField(max_length=255, blank=True, null=True)
    lid1 = models.CharField(max_length=255)
    f002 = models.DateField(blank=True, null=True)
    e001 = models.CharField(max_length=255, blank=True, null=True)
    e002 = models.CharField(max_length=255, blank=True, null=True)
    f003 = models.DateField(blank=True, null=True)
    f004 = models.DateField()
    aprob1 = models.CharField(max_length=255, blank=True, null=True)
    com1 = models.CharField(max_length=255, blank=True, null=True)
    e003 = models.IntegerField(blank=True, null=True)
    lid2 = models.CharField(max_length=255)
    ger001 = models.CharField(max_length=255)
    p001 = models.CharField(max_length=255)
    c001 = models.CharField(max_length=255)
    c002 = models.CharField(max_length=255)
    i001 = models.CharField(max_length=255)
    a001 = models.CharField(max_length=255)
    m001 = models.CharField(max_length=255)
    f005 = models.CharField(max_length=255)
    ti001 = models.CharField(max_length=255)
    tt001 = models.CharField(max_length=255)
    cc001 = models.IntegerField()
    tc001 = models.CharField(max_length=255)
    cc002 = models.IntegerField()
    tp001 = models.CharField(max_length=255)
    h001 = models.CharField(max_length=255)
    sc001 = models.CharField(max_length=255)
    io001 = models.CharField(max_length=255)
    m002 = models.IntegerField()
    e005 = models.DateField(blank=True, null=True)
    p002 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'llxdx_projet_extrafields'


class LlxdxProjetTask(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=50, blank=True, null=True)
    entity = models.IntegerField()
    fk_projet = models.ForeignKey(LlxdxProjet, models.DO_NOTHING, db_column='fk_projet')
    fk_task_parent = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    dateo = models.DateTimeField(blank=True, null=True)
    datee = models.DateTimeField(blank=True, null=True)
    datev = models.DateTimeField(blank=True, null=True)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration_effective = models.FloatField(blank=True, null=True)
    planned_workload = models.FloatField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    budget_amount = models.FloatField(blank=True, null=True)
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat', blank=True, null=True)
    fk_user_valid = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_valid', related_name='llxdxprojettask_fk_user_valid_set', blank=True, null=True)
    fk_statut = models.SmallIntegerField()
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_projet_task'
        unique_together = (('ref', 'entity'),)


class LlxdxProjetTaskExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    t001 = models.CharField(max_length=255, blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    verif = models.IntegerField(blank=True, null=True)
    proced = models.IntegerField(blank=True, null=True)
    verif01 = models.CharField(max_length=255, blank=True, null=True)
    proced01 = models.CharField(max_length=255, blank=True, null=True)
    valid01 = models.CharField(max_length=255, blank=True, null=True)
    t004 = models.CharField(max_length=255)
    tipotarea = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_projet_task_extrafields'


class LlxdxPropal(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_int = models.CharField(max_length=255, blank=True, null=True)
    ref_client = models.CharField(max_length=255, blank=True, null=True)
    fk_soc = models.ForeignKey('LlxdxSociete', models.DO_NOTHING, db_column='fk_soc', blank=True, null=True)
    fk_projet = models.ForeignKey(LlxdxProjet, models.DO_NOTHING, db_column='fk_projet', blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    datep = models.DateField(blank=True, null=True)
    fin_validite = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    date_signature = models.DateTimeField(blank=True, null=True)
    date_cloture = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_author', blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_valid', related_name='llxdxpropal_fk_user_valid_set', blank=True, null=True)
    fk_user_signature = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_signature', related_name='llxdxpropal_fk_user_signature_set', blank=True, null=True)
    fk_user_cloture = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_cloture', related_name='llxdxpropal_fk_user_cloture_set', blank=True, null=True)
    fk_statut = models.SmallIntegerField()
    price = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise_absolue = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_currency = models.CharField(max_length=3, blank=True, null=True)
    fk_cond_reglement = models.IntegerField(blank=True, null=True)
    deposit_percent = models.CharField(max_length=63, blank=True, null=True)
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    date_livraison = models.DateField(blank=True, null=True)
    fk_shipping_method = models.IntegerField(blank=True, null=True)
    fk_warehouse = models.IntegerField(blank=True, null=True)
    fk_availability = models.IntegerField(blank=True, null=True)
    fk_input_reason = models.IntegerField(blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_delivery_address = models.IntegerField(blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    online_sign_ip = models.CharField(max_length=48, blank=True, null=True)
    online_sign_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_propal'
        unique_together = (('ref', 'entity'),)


class LlxdxPropalExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_propal_extrafields'


class LlxdxPropalMergePdfProduct(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_product = models.IntegerField()
    file_name = models.CharField(max_length=200)
    lang = models.CharField(max_length=5, blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_mod = models.IntegerField()
    datec = models.DateTimeField()
    tms = models.DateTimeField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_propal_merge_pdf_product'


class LlxdxPropaldet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_propal = models.ForeignKey(LlxdxPropal, models.DO_NOTHING, db_column='fk_propal')
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    buy_price_ht = models.FloatField(blank=True, null=True)
    fk_product_fournisseur_price = models.IntegerField(blank=True, null=True)
    special_code = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_propaldet'


class LlxdxPropaldetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_propaldet_extrafields'


class LlxdxReception(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    fk_soc = models.IntegerField()
    fk_projet = models.IntegerField(blank=True, null=True)
    ref_ext = models.CharField(max_length=30, blank=True, null=True)
    ref_int = models.CharField(max_length=30, blank=True, null=True)
    ref_supplier = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    date_delivery = models.DateTimeField(blank=True, null=True)
    date_reception = models.DateTimeField(blank=True, null=True)
    fk_shipping_method = models.IntegerField(blank=True, null=True)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    fk_statut = models.SmallIntegerField(blank=True, null=True)
    billed = models.SmallIntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    size_units = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    weight_units = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_reception'
        unique_together = (('ref', 'entity'),)


class LlxdxReceptionExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_reception_extrafields'


class LlxdxRecruitmentRecruitmentcandidature(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_recruitmentjobposition = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField()
    firstname = models.CharField(max_length=128, blank=True, null=True)
    lastname = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    remuneration_requested = models.IntegerField(blank=True, null=True)
    remuneration_proposed = models.IntegerField(blank=True, null=True)
    email_msgid = models.CharField(unique=True, max_length=175, blank=True, null=True)
    email_date = models.DateTimeField(blank=True, null=True)
    fk_recruitment_origin = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_recruitment_recruitmentcandidature'


class LlxdxRecruitmentRecruitmentcandidatureExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_recruitment_recruitmentcandidature_extrafields'


class LlxdxRecruitmentRecruitmentjobposition(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    entity = models.IntegerField()
    label = models.CharField(max_length=255)
    qty = models.IntegerField()
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_project = models.IntegerField(blank=True, null=True)
    fk_user_recruiter = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_recruiter', blank=True, null=True)
    fk_user_supervisor = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_supervisor', related_name='llxdxrecruitmentrecruitmentjobposition_fk_user_supervisor_set', blank=True, null=True)
    fk_establishment = models.ForeignKey(LlxdxEstablishment, models.DO_NOTHING, db_column='fk_establishment', blank=True, null=True)
    date_planned = models.DateField(blank=True, null=True)
    remuneration_suggested = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat', related_name='llxdxrecruitmentrecruitmentjobposition_fk_user_creat_set')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField()
    email_recruiter = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_recruitment_recruitmentjobposition'


class LlxdxRecruitmentRecruitmentjobpositionExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_recruitment_recruitmentjobposition_extrafields'


class LlxdxResource(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref = models.CharField(max_length=255, blank=True, null=True)
    asset_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fk_code_type_resource = models.CharField(max_length=32, blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    fk_statut = models.SmallIntegerField()
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    tms = models.DateTimeField()
    fk_country = models.ForeignKey(LlxdxCCountry, models.DO_NOTHING, db_column='fk_country', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_resource'
        unique_together = (('ref', 'entity'),)


class LlxdxResourceExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_resource_extrafields'


class LlxdxRightsDef(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, entity) found, that is not supported. The first column is selected.
    libelle = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=64, blank=True, null=True)
    entity = models.IntegerField()
    perms = models.CharField(max_length=50, blank=True, null=True)
    subperms = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    bydefault = models.IntegerField(blank=True, null=True)
    module_position = models.IntegerField()
    family_position = models.IntegerField()
    tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llxdx_rights_def'
        unique_together = (('id', 'entity'),)


class LlxdxSalary(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    fk_user = models.IntegerField()
    datep = models.DateField(blank=True, null=True)
    datev = models.DateField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    amount = models.FloatField()
    fk_projet = models.IntegerField(blank=True, null=True)
    datesp = models.DateField(blank=True, null=True)
    dateep = models.DateField(blank=True, null=True)
    entity = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField(blank=True, null=True)
    paye = models.SmallIntegerField()
    fk_typepayment = models.IntegerField()
    fk_account = models.IntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_salary'


class LlxdxSalaryExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_salary_extrafields'


class LlxdxSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=50)
    session_variable = models.TextField(blank=True, null=True)
    last_accessed = models.DateTimeField()
    fk_user = models.IntegerField()
    remote_ip = models.CharField(max_length=64, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_session'


class LlxdxSociete(models.Model):
    rowid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=128, blank=True, null=True)
    name_alias = models.CharField(max_length=128, blank=True, null=True)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_int = models.CharField(max_length=60, blank=True, null=True)
    statut = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    code_client = models.CharField(max_length=24, blank=True, null=True)
    code_fournisseur = models.CharField(max_length=24, blank=True, null=True)
    code_compta = models.CharField(max_length=24, blank=True, null=True)
    code_compta_fournisseur = models.CharField(max_length=24, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=25, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    fk_departement = models.IntegerField(blank=True, null=True)
    fk_pays = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    socialnetworks = models.TextField(blank=True, null=True)
    fk_effectif = models.IntegerField(blank=True, null=True)
    fk_typent = models.IntegerField(blank=True, null=True)
    fk_forme_juridique = models.IntegerField(blank=True, null=True)
    fk_currency = models.CharField(max_length=3, blank=True, null=True)
    siren = models.CharField(max_length=128, blank=True, null=True)
    siret = models.CharField(max_length=128, blank=True, null=True)
    ape = models.CharField(max_length=128, blank=True, null=True)
    idprof4 = models.CharField(max_length=128, blank=True, null=True)
    idprof5 = models.CharField(max_length=128, blank=True, null=True)
    idprof6 = models.CharField(max_length=128, blank=True, null=True)
    tva_intra = models.CharField(max_length=20, blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    fk_stcomm = models.IntegerField()
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)
    prefix_comm = models.CharField(max_length=5, blank=True, null=True)
    client = models.IntegerField(blank=True, null=True)
    fournisseur = models.IntegerField(blank=True, null=True)
    supplier_account = models.CharField(max_length=32, blank=True, null=True)
    fk_prospectlevel = models.CharField(max_length=12, blank=True, null=True)
    fk_incoterms = models.IntegerField(blank=True, null=True)
    location_incoterms = models.CharField(max_length=255, blank=True, null=True)
    customer_bad = models.IntegerField(blank=True, null=True)
    customer_rate = models.FloatField(blank=True, null=True)
    supplier_rate = models.FloatField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    remise_client = models.FloatField(blank=True, null=True)
    remise_supplier = models.FloatField(blank=True, null=True)
    mode_reglement = models.IntegerField(blank=True, null=True)
    cond_reglement = models.IntegerField(blank=True, null=True)
    deposit_percent = models.CharField(max_length=63, blank=True, null=True)
    transport_mode = models.IntegerField(blank=True, null=True)
    mode_reglement_supplier = models.IntegerField(blank=True, null=True)
    cond_reglement_supplier = models.IntegerField(blank=True, null=True)
    transport_mode_supplier = models.IntegerField(blank=True, null=True)
    fk_shipping_method = models.IntegerField(blank=True, null=True)
    tva_assuj = models.IntegerField(blank=True, null=True)
    vat_reverse_charge = models.IntegerField(blank=True, null=True)
    localtax1_assuj = models.IntegerField(blank=True, null=True)
    localtax1_value = models.FloatField(blank=True, null=True)
    localtax2_assuj = models.IntegerField(blank=True, null=True)
    localtax2_value = models.FloatField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    fk_barcode_type = models.IntegerField(blank=True, null=True)
    price_level = models.IntegerField(blank=True, null=True)
    outstanding_limit = models.FloatField(blank=True, null=True)
    order_min_amount = models.FloatField(blank=True, null=True)
    supplier_order_min_amount = models.FloatField(blank=True, null=True)
    default_lang = models.CharField(max_length=6, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    canvas = models.CharField(max_length=32, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    webservices_url = models.CharField(max_length=255, blank=True, null=True)
    webservices_key = models.CharField(max_length=128, blank=True, null=True)
    accountancy_code_sell = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy = models.CharField(max_length=32, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_warehouse = models.IntegerField(blank=True, null=True)
    logo_squarred = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe'
        unique_together = (('barcode', 'fk_barcode_type', 'entity'), ('prefix_comm', 'entity'), ('code_fournisseur', 'entity'), ('code_client', 'entity'),)


class LlxdxSocieteAccount(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    key_account = models.CharField(max_length=128, blank=True, null=True)
    login = models.CharField(max_length=128)
    pass_encoding = models.CharField(max_length=24, blank=True, null=True)
    pass_crypted = models.CharField(max_length=128, blank=True, null=True)
    pass_temp = models.CharField(max_length=128, blank=True, null=True)
    fk_soc = models.ForeignKey(LlxdxSociete, models.DO_NOTHING, db_column='fk_soc', blank=True, null=True)
    site = models.CharField(max_length=128, blank=True, null=True)
    fk_website = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_last_login = models.DateTimeField(blank=True, null=True)
    date_previous_login = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField()
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    site_account = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_account'
        unique_together = (('entity', 'fk_soc', 'login', 'site', 'fk_website'), ('entity', 'fk_soc', 'key_account', 'site', 'fk_website'),)


class LlxdxSocieteAddress(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    label = models.CharField(max_length=30, blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    fk_pays = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_address'


class LlxdxSocieteCommerciaux(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_commerciaux'
        unique_together = (('fk_soc', 'fk_user'),)


class LlxdxSocieteContacts(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    date_creation = models.DateTimeField()
    fk_soc = models.ForeignKey(LlxdxSociete, models.DO_NOTHING, db_column='fk_soc')
    fk_c_type_contact = models.ForeignKey(LlxdxCTypeContact, models.DO_NOTHING, db_column='fk_c_type_contact')
    fk_socpeople = models.ForeignKey('LlxdxSocpeople', models.DO_NOTHING, db_column='fk_socpeople')
    tms = models.DateTimeField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_contacts'
        unique_together = (('entity', 'fk_soc', 'fk_c_type_contact', 'fk_socpeople'),)


class LlxdxSocieteExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField(unique=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_extrafields'


class LlxdxSocieteLog(models.Model):
    datel = models.DateTimeField(blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_statut = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    label = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_log'


class LlxdxSocietePerentity(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    entity = models.IntegerField()
    accountancy_code_customer = models.CharField(max_length=24, blank=True, null=True)
    accountancy_code_supplier = models.CharField(max_length=24, blank=True, null=True)
    accountancy_code_sell = models.CharField(max_length=32, blank=True, null=True)
    accountancy_code_buy = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_perentity'
        unique_together = (('fk_soc', 'entity'),)


class LlxdxSocietePrices(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    price_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_prices'


class LlxdxSocieteRemise(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_soc = models.IntegerField()
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    remise_client = models.FloatField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_remise'


class LlxdxSocieteRemiseExcept(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_soc = models.ForeignKey(LlxdxSociete, models.DO_NOTHING, db_column='fk_soc')
    discount_type = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    amount_ht = models.FloatField()
    amount_tva = models.FloatField()
    amount_ttc = models.FloatField()
    tva_tx = models.FloatField()
    fk_user = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user')
    fk_facture_line = models.ForeignKey(LlxdxFacturedet, models.DO_NOTHING, db_column='fk_facture_line', blank=True, null=True)
    fk_facture = models.ForeignKey(LlxdxFacture, models.DO_NOTHING, db_column='fk_facture', blank=True, null=True)
    fk_facture_source = models.ForeignKey(LlxdxFacture, models.DO_NOTHING, db_column='fk_facture_source', related_name='llxdxsocieteremiseexcept_fk_facture_source_set', blank=True, null=True)
    description = models.TextField()
    multicurrency_amount_ht = models.FloatField()
    multicurrency_amount_tva = models.FloatField()
    multicurrency_amount_ttc = models.FloatField()
    fk_invoice_supplier_line = models.ForeignKey(LlxdxFactureFournDet, models.DO_NOTHING, db_column='fk_invoice_supplier_line', blank=True, null=True)
    fk_invoice_supplier = models.ForeignKey(LlxdxFactureFourn, models.DO_NOTHING, db_column='fk_invoice_supplier', blank=True, null=True)
    fk_invoice_supplier_source = models.IntegerField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_remise_except'


class LlxdxSocieteRemiseSupplier(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_soc = models.IntegerField()
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    remise_supplier = models.FloatField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_remise_supplier'


class LlxdxSocieteRib(models.Model):
    rowid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    fk_soc = models.ForeignKey(LlxdxSociete, models.DO_NOTHING, db_column='fk_soc')
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    label = models.CharField(max_length=200, blank=True, null=True)
    bank = models.CharField(max_length=255, blank=True, null=True)
    code_banque = models.CharField(max_length=128, blank=True, null=True)
    code_guichet = models.CharField(max_length=6, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    cle_rib = models.CharField(max_length=5, blank=True, null=True)
    bic = models.CharField(max_length=20, blank=True, null=True)
    iban_prefix = models.CharField(max_length=34, blank=True, null=True)
    domiciliation = models.CharField(max_length=255, blank=True, null=True)
    proprio = models.CharField(max_length=60, blank=True, null=True)
    owner_address = models.CharField(max_length=255, blank=True, null=True)
    default_rib = models.SmallIntegerField()
    state_id = models.IntegerField(blank=True, null=True)
    fk_country = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=3, blank=True, null=True)
    rum = models.CharField(max_length=32, blank=True, null=True)
    date_rum = models.DateField(blank=True, null=True)
    frstrecur = models.CharField(max_length=16, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    last_four = models.CharField(max_length=4, blank=True, null=True)
    card_type = models.CharField(max_length=255, blank=True, null=True)
    cvn = models.CharField(max_length=255, blank=True, null=True)
    exp_date_month = models.IntegerField(blank=True, null=True)
    exp_date_year = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    max_total_amount_of_all_payments = models.FloatField(blank=True, null=True)
    preapproval_key = models.CharField(max_length=255, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    total_amount_of_all_payments = models.FloatField(blank=True, null=True)
    stripe_card_ref = models.CharField(max_length=128, blank=True, null=True)
    status = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    ipaddress = models.CharField(max_length=68, blank=True, null=True)
    stripe_account = models.CharField(max_length=128, blank=True, null=True)
    ext_payment_site = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_societe_rib'


class LlxdxSocpeople(models.Model):
    rowid = models.AutoField(primary_key=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_soc = models.ForeignKey(LlxdxSociete, models.DO_NOTHING, db_column='fk_soc', blank=True, null=True)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    civility = models.CharField(max_length=6, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=25, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    fk_departement = models.IntegerField(blank=True, null=True)
    fk_pays = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    poste = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    phone_perso = models.CharField(max_length=30, blank=True, null=True)
    phone_mobile = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    socialnetworks = models.TextField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    no_email = models.SmallIntegerField()
    priv = models.SmallIntegerField()
    fk_prospectlevel = models.CharField(max_length=12, blank=True, null=True)
    fk_stcommcontact = models.IntegerField()
    fk_user_creat = models.ForeignKey('LlxdxUser', models.DO_NOTHING, db_column='fk_user_creat', blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    default_lang = models.CharField(max_length=6, blank=True, null=True)
    canvas = models.CharField(max_length=32, blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_socpeople'


class LlxdxSocpeopleExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_socpeople_extrafields'


class LlxdxStockMouvement(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    datem = models.DateTimeField(blank=True, null=True)
    fk_product = models.IntegerField()
    batch = models.CharField(max_length=128, blank=True, null=True)
    eatby = models.DateField(blank=True, null=True)
    sellby = models.DateField(blank=True, null=True)
    fk_entrepot = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    type_mouvement = models.SmallIntegerField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    inventorycode = models.CharField(max_length=128, blank=True, null=True)
    fk_origin = models.IntegerField(blank=True, null=True)
    origintype = models.CharField(max_length=64, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    fk_projet = models.IntegerField()
    fk_project = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_stock_mouvement'


class LlxdxStockMouvementExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_stock_mouvement_extrafields'


class LlxdxSubscription(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    fk_adherent = models.IntegerField(blank=True, null=True)
    dateadh = models.DateTimeField(blank=True, null=True)
    datef = models.DateTimeField(blank=True, null=True)
    subscription = models.FloatField(blank=True, null=True)
    fk_bank = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_type = models.IntegerField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_subscription'
        unique_together = (('fk_adherent', 'dateadh'), ('fk_adherent', 'dateadh'),)


class LlxdxSupplierProposal(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=30)
    entity = models.IntegerField()
    ref_ext = models.CharField(max_length=255, blank=True, null=True)
    ref_int = models.CharField(max_length=255, blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_projet = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    datec = models.DateTimeField(blank=True, null=True)
    date_valid = models.DateTimeField(blank=True, null=True)
    date_cloture = models.DateTimeField(blank=True, null=True)
    fk_user_author = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    fk_user_valid = models.IntegerField(blank=True, null=True)
    fk_user_cloture = models.IntegerField(blank=True, null=True)
    fk_statut = models.SmallIntegerField()
    price = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise_absolue = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    localtax1 = models.FloatField(blank=True, null=True)
    localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    fk_account = models.IntegerField(blank=True, null=True)
    fk_currency = models.CharField(max_length=3, blank=True, null=True)
    fk_cond_reglement = models.IntegerField(blank=True, null=True)
    fk_mode_reglement = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    date_livraison = models.DateField(blank=True, null=True)
    fk_shipping_method = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    extraparams = models.CharField(max_length=255, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_tx = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    last_main_doc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_supplier_proposal'
        unique_together = (('ref', 'entity'),)


class LlxdxSupplierProposalExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_supplier_proposal_extrafields'


class LlxdxSupplierProposaldet(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_supplier_proposal = models.ForeignKey(LlxdxSupplierProposal, models.DO_NOTHING, db_column='fk_supplier_proposal')
    fk_parent_line = models.IntegerField(blank=True, null=True)
    fk_product = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fk_remise_except = models.IntegerField(blank=True, null=True)
    tva_tx = models.FloatField(blank=True, null=True)
    vat_src_code = models.CharField(max_length=10, blank=True, null=True)
    localtax1_tx = models.FloatField(blank=True, null=True)
    localtax1_type = models.CharField(max_length=10, blank=True, null=True)
    localtax2_tx = models.FloatField(blank=True, null=True)
    localtax2_type = models.CharField(max_length=10, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    remise_percent = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    subprice = models.FloatField(blank=True, null=True)
    total_ht = models.FloatField(blank=True, null=True)
    total_tva = models.FloatField(blank=True, null=True)
    total_localtax1 = models.FloatField(blank=True, null=True)
    total_localtax2 = models.FloatField(blank=True, null=True)
    total_ttc = models.FloatField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    info_bits = models.IntegerField(blank=True, null=True)
    buy_price_ht = models.FloatField(blank=True, null=True)
    fk_product_fournisseur_price = models.IntegerField(blank=True, null=True)
    special_code = models.IntegerField(blank=True, null=True)
    rang = models.IntegerField(blank=True, null=True)
    ref_fourn = models.CharField(max_length=30, blank=True, null=True)
    fk_multicurrency = models.IntegerField(blank=True, null=True)
    multicurrency_code = models.CharField(max_length=3, blank=True, null=True)
    multicurrency_subprice = models.FloatField(blank=True, null=True)
    multicurrency_total_ht = models.FloatField(blank=True, null=True)
    multicurrency_total_tva = models.FloatField(blank=True, null=True)
    multicurrency_total_ttc = models.FloatField(blank=True, null=True)
    fk_unit = models.ForeignKey(LlxdxCUnits, models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_supplier_proposaldet'


class LlxdxSupplierProposaldetExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_supplier_proposaldet_extrafields'


class LlxdxTakeposFloorTables(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    leftpos = models.FloatField(blank=True, null=True)
    toppos = models.FloatField(blank=True, null=True)
    floor = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_takepos_floor_tables'
        unique_together = (('entity', 'label'),)


class LlxdxTicket(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=128)
    track_id = models.CharField(unique=True, max_length=128)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_project = models.IntegerField(blank=True, null=True)
    origin_email = models.CharField(max_length=128, blank=True, null=True)
    fk_user_create = models.IntegerField(blank=True, null=True)
    fk_user_assign = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    fk_statut = models.IntegerField(blank=True, null=True)
    resolution = models.IntegerField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    timing = models.CharField(max_length=20, blank=True, null=True)
    type_code = models.CharField(max_length=32, blank=True, null=True)
    category_code = models.CharField(max_length=32, blank=True, null=True)
    severity_code = models.CharField(max_length=32, blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    date_read = models.DateTimeField(blank=True, null=True)
    date_last_msg_sent = models.DateTimeField(blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    notify_tiers_at_create = models.IntegerField(blank=True, null=True)
    tms = models.DateTimeField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    email_msgid = models.CharField(max_length=255, blank=True, null=True)
    email_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_ticket'
        unique_together = (('ref', 'entity'),)


class LlxdxTicketExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)
    fechadenecesidad = models.DateField()
    ticketexpost = models.IntegerField(blank=True, null=True)
    solicitante = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_ticket_extrafields'


class LlxdxTreeTask(models.Model):
    id_tarea = models.IntegerField(db_column='ID_Tarea', primary_key=True)  # Field name made lowercase.
    cod_tarea = models.CharField(db_column='Cod_tarea', max_length=45, blank=True, null=True)  # Field name made lowercase.
    desc_tarea = models.CharField(db_column='Desc_Tarea', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tarea_cuenta = models.CharField(db_column='Tarea_Cuenta', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'llxdx_tree_task'


class LlxdxTva(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    datec = models.DateField(blank=True, null=True)
    datep = models.DateField(blank=True, null=True)
    datev = models.DateField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    fk_typepayment = models.IntegerField(blank=True, null=True)
    num_payment = models.CharField(max_length=50, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    entity = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    fk_bank = models.IntegerField(blank=True, null=True)
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    paye = models.SmallIntegerField()
    fk_account = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_tva'


class LlxdxUser(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref_employee = models.CharField(max_length=50, blank=True, null=True)
    ref_ext = models.CharField(max_length=50, blank=True, null=True)
    employee = models.IntegerField(blank=True, null=True)
    fk_establishment = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    login = models.CharField(max_length=50)
    pass_field = models.CharField(db_column='pass', max_length=128, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    pass_crypted = models.CharField(max_length=128, blank=True, null=True)
    pass_temp = models.CharField(max_length=128, blank=True, null=True)
    api_key = models.CharField(unique=True, max_length=128, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    civility = models.CharField(max_length=6, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=25, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    fk_state = models.IntegerField(blank=True, null=True)
    fk_country = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=128, blank=True, null=True)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    office_fax = models.CharField(max_length=20, blank=True, null=True)
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    personal_mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    personal_email = models.CharField(max_length=255, blank=True, null=True)
    socialnetworks = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    admin = models.SmallIntegerField(blank=True, null=True)
    fk_soc = models.IntegerField(blank=True, null=True)
    fk_socpeople = models.IntegerField(unique=True, blank=True, null=True)
    fk_member = models.IntegerField(unique=True, blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    fk_user_expense_validator = models.IntegerField(blank=True, null=True)
    fk_user_holiday_validator = models.IntegerField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    datelastlogin = models.DateTimeField(blank=True, null=True)
    datepreviouslogin = models.DateTimeField(blank=True, null=True)
    egroupware_id = models.IntegerField(blank=True, null=True)
    ldap_sid = models.CharField(max_length=255, blank=True, null=True)
    openid = models.CharField(max_length=255, blank=True, null=True)
    statut = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=6, blank=True, null=True)
    color = models.CharField(max_length=6, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    fk_barcode_type = models.IntegerField(blank=True, null=True)
    accountancy_code = models.CharField(max_length=32, blank=True, null=True)
    nb_holiday = models.IntegerField(blank=True, null=True)
    thm = models.FloatField(blank=True, null=True)
    tjm = models.FloatField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    salaryextra = models.FloatField(blank=True, null=True)
    weeklyhours = models.FloatField(blank=True, null=True)
    dateemployment = models.DateTimeField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    pass_encoding = models.CharField(max_length=24, blank=True, null=True)
    default_range = models.IntegerField(blank=True, null=True)
    default_c_exp_tax_cat = models.IntegerField(blank=True, null=True)
    dateemploymentend = models.DateField(blank=True, null=True)
    fk_warehouse = models.IntegerField(blank=True, null=True)
    iplastlogin = models.CharField(max_length=250, blank=True, null=True)
    ippreviouslogin = models.CharField(max_length=250, blank=True, null=True)
    datelastpassvalidation = models.DateTimeField(blank=True, null=True)
    datestartvalidity = models.DateTimeField(blank=True, null=True)
    dateendvalidity = models.DateTimeField(blank=True, null=True)
    national_registration_number = models.CharField(max_length=50, blank=True, null=True)
    birth_place = models.CharField(max_length=64, blank=True, null=True)
    flagdelsessionsbefore = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_user'
        unique_together = (('login', 'entity'),)


class LlxdxUserAlert(models.Model):
    rowid = models.AutoField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    fk_contact = models.IntegerField(blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_user_alert'


class LlxdxUserClicktodial(models.Model):
    fk_user = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=32, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=64, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    poste = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_user_clicktodial'


class LlxdxUserEmployment(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref = models.CharField(max_length=50, blank=True, null=True)
    ref_ext = models.CharField(max_length=50, blank=True, null=True)
    fk_user = models.IntegerField(blank=True, null=True)
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=128, blank=True, null=True)
    status = models.IntegerField()
    salary = models.FloatField(blank=True, null=True)
    salaryextra = models.FloatField(blank=True, null=True)
    weeklyhours = models.FloatField(blank=True, null=True)
    dateemployment = models.DateField(blank=True, null=True)
    dateemploymentend = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_user_employment'


class LlxdxUserExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_user_extrafields'


class LlxdxUserParam(models.Model):
    fk_user = models.IntegerField()
    entity = models.IntegerField()
    param = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'llxdx_user_param'
        unique_together = (('fk_user', 'param', 'entity'),)


class LlxdxUserRib(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_user = models.IntegerField()
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    label = models.CharField(max_length=30, blank=True, null=True)
    bank = models.CharField(max_length=255, blank=True, null=True)
    code_banque = models.CharField(max_length=128, blank=True, null=True)
    code_guichet = models.CharField(max_length=6, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    cle_rib = models.CharField(max_length=5, blank=True, null=True)
    bic = models.CharField(max_length=11, blank=True, null=True)
    iban_prefix = models.CharField(max_length=34, blank=True, null=True)
    domiciliation = models.CharField(max_length=255, blank=True, null=True)
    proprio = models.CharField(max_length=60, blank=True, null=True)
    owner_address = models.CharField(max_length=255, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    fk_country = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_user_rib'


class LlxdxUserRights(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_user = models.ForeignKey(LlxdxUser, models.DO_NOTHING, db_column='fk_user')
    fk_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_user_rights'
        unique_together = (('entity', 'fk_user', 'fk_id'),)


class LlxdxUsergroup(models.Model):
    rowid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    entity = models.IntegerField()
    datec = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    model_pdf = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_usergroup'
        unique_together = (('nom', 'entity'),)


class LlxdxUsergroupExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_usergroup_extrafields'


class LlxdxUsergroupRights(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_usergroup = models.ForeignKey(LlxdxUsergroup, models.DO_NOTHING, db_column='fk_usergroup')
    fk_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'llxdx_usergroup_rights'
        unique_together = (('entity', 'fk_usergroup', 'fk_id'),)


class LlxdxUsergroupUser(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    fk_user = models.ForeignKey(LlxdxUser, models.DO_NOTHING, db_column='fk_user')
    fk_usergroup = models.ForeignKey(LlxdxUsergroup, models.DO_NOTHING, db_column='fk_usergroup')

    class Meta:
        managed = False
        db_table = 'llxdx_usergroup_user'
        unique_together = (('entity', 'fk_user', 'fk_usergroup'),)


class LlxdxWebsite(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    ref = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    fk_default_home = models.IntegerField(blank=True, null=True)
    virtualhost = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    maincolor = models.CharField(max_length=16, blank=True, null=True)
    maincolorbis = models.CharField(max_length=16, blank=True, null=True)
    use_manifest = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=8, blank=True, null=True)
    otherlang = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    lastaccess = models.DateTimeField(blank=True, null=True)
    pageviews_month = models.PositiveBigIntegerField(blank=True, null=True)
    pageviews_total = models.PositiveBigIntegerField(blank=True, null=True)
    pageviews_previous_month = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_website'
        unique_together = (('ref', 'entity'),)


class LlxdxWebsiteExtrafields(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_object = models.IntegerField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_website_extrafields'


class LlxdxWebsitePage(models.Model):
    rowid = models.AutoField(primary_key=True)
    fk_website = models.ForeignKey(LlxdxWebsite, models.DO_NOTHING, db_column='fk_website')
    pageurl = models.CharField(max_length=255, blank=True, null=True)
    aliasalt = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    tms = models.DateTimeField()
    fk_user_creat = models.IntegerField(blank=True, null=True)
    fk_user_modif = models.IntegerField(blank=True, null=True)
    type_container = models.CharField(max_length=16)
    lang = models.CharField(max_length=6, blank=True, null=True)
    fk_page = models.IntegerField(blank=True, null=True)
    grabbed_from = models.CharField(max_length=255, blank=True, null=True)
    htmlheader = models.TextField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    author_alias = models.CharField(max_length=64, blank=True, null=True)
    allowed_in_frames = models.IntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=255, blank=True, null=True)
    fk_object = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_website_page'
        unique_together = (('fk_website', 'pageurl'),)


class LlxdxWorkstationWorkstation(models.Model):
    rowid = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=128)
    label = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)
    entity = models.IntegerField(blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField()
    tms = models.DateTimeField()
    fk_user_creat = models.ForeignKey(LlxdxUser, models.DO_NOTHING, db_column='fk_user_creat')
    fk_user_modif = models.IntegerField(blank=True, null=True)
    import_key = models.CharField(max_length=14, blank=True, null=True)
    status = models.SmallIntegerField()
    nb_operators_required = models.IntegerField(blank=True, null=True)
    thm_operator_estimated = models.FloatField(blank=True, null=True)
    thm_machine_estimated = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_workstation_workstation'


class LlxdxWorkstationWorkstationResource(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_resource = models.IntegerField(blank=True, null=True)
    fk_workstation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_workstation_workstation_resource'


class LlxdxWorkstationWorkstationUsergroup(models.Model):
    rowid = models.AutoField(primary_key=True)
    tms = models.DateTimeField()
    fk_usergroup = models.IntegerField(blank=True, null=True)
    fk_workstation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_workstation_workstation_usergroup'


class LlxdxZapierHook(models.Model):
    rowid = models.AutoField(primary_key=True)
    entity = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=128, blank=True, null=True)
    action = models.CharField(max_length=128, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField()
    fk_user = models.IntegerField()
    tms = models.DateTimeField()
    import_key = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llxdx_zapier_hook'


class TmpLlxdxAccoutingAccount(models.Model):
    minid = models.IntegerField(db_column='MINID', blank=True, null=True)  # Field name made lowercase.
    maxid = models.IntegerField(db_column='MAXID', blank=True, null=True)  # Field name made lowercase.
    account_number = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')
    entity = models.IntegerField()
    fk_pcg_version = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')
    nb = models.BigIntegerField(db_column='NB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_llxdx_accouting_account'
