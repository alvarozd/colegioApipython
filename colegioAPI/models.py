from django.db import models


class Actividad(models.Model):
    idactividad = models.AutoField(db_column='idActividad', primary_key=True)  # Field name made lowercase.
    nombreactividad = models.CharField(db_column='nombreActividad', max_length=200, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idmateria = models.ForeignKey('Materia', models.DO_NOTHING, db_column='idMateria', blank=True, null=True)  # Field name made lowercase.
    fechainicial = models.CharField(db_column='fechaInicial', max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.CharField(db_column='fechaFinal', max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'


class ActividadPeriodo(models.Model):
    idperiodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='idPeriodo', blank=True, null=True)  # Field name made lowercase.
    idactividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='idActividad', blank=True, null=True)  # Field name made lowercase.
    idestudiante = models.ForeignKey('Persona', models.DO_NOTHING, db_column='idEstudiante', blank=True, null=True)  # Field name made lowercase.
    calificacion = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad_periodo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Modern_Spanish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Modern_Spanish_CI_AS')
    session_data = models.TextField(db_collation='Modern_Spanish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Grado(models.Model):
    idgrado = models.AutoField(db_column='idGrado', primary_key=True)  # Field name made lowercase.
    numerogrado = models.CharField(db_column='numeroGrado', max_length=15, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    def save(self, *args, **kwargs):
        # Eliminar espacios en blanco al final del numeroGrado
        if self.numerogrado:
            self.numerogrado = self.numerogrado.strip()
        super().save(*args, **kwargs)
        
    class Meta:
        managed = False
        db_table = 'grado'


class Materia(models.Model):
    idmateria = models.AutoField(db_column='idMateria', primary_key=True)  # Field name made lowercase.
    idgrado = models.ForeignKey(Grado, models.DO_NOTHING, db_column='idGrado', blank=True, null=True)  # Field name made lowercase.
    nombremateria = models.CharField(db_column='nombreMateria', max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia'


class Periodo(models.Model):
    idperiodo = models.AutoField(db_column='idPeriodo', primary_key=True)  # Field name made lowercase.
    nombreperiodo = models.CharField(db_column='nombrePeriodo', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechainicial = models.CharField(db_column='fechaInicial', max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.CharField(db_column='fechaFinal', max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    documento = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    primernombre = models.CharField(db_column='primerNombre', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='primerApellido', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='segundoApellido', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='idRol')  # Field name made lowercase.
    idsexo = models.ForeignKey('Sexo', models.DO_NOTHING, db_column='idSexo')  # Field name made lowercase.
    fotografia = models.CharField(max_length=300, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    telefono = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    correo = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    contrasena = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    idgrado = models.ForeignKey(Grado, models.DO_NOTHING, db_column='idGrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class ResponsableEstudiante(models.Model):
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idpersona', blank=True, null=True)
    idestudiante = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idestudiante', related_name='responsableestudiante_idestudiante_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responsable_estudiante'


class Rol(models.Model):
    idrol = models.AutoField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    nombrerol = models.CharField(db_column='nombreRol', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rol'


class Sexo(models.Model):
    idsexo = models.AutoField(db_column='idSexo', primary_key=True)  # Field name made lowercase.
    nombresexo = models.CharField(db_column='nombreSexo', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sexo'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
