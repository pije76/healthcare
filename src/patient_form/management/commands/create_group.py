from django.contrib.auth.models import Group, Permission
#from django.contrib.auth.models import ContentType
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.db.models import signals


import logging

from accounts.models import UserProfile
#from ...models import *
from patient_form import models

#GROUPS = ['patient', 'staff']
#MODELS = ['patient_form']
#PERMISSIONS = ['view', ]

#GROUPS_PERMISSIONS = {
#	'patient_form': {
#		models.Admission: ['add', 'change', 'delete', 'view'],
#	},
#}

class Command(BaseCommand):
	def __init__(self, *args, **kwargs):
		super(Command, self).__init__(*args, **kwargs)

	help = 'Creates read only default permission groups for users'

#	def create_user_groups(app, created_models, verbosity, **kwargs):
	def handle(self, *args, **options):
#		content_type = ContentType.objects.get(app_label='patient_form', model='Admission')
#		perms = Permission.objects.filter(content_type=content_type)
#		perms = Permission.objects.all()
#		perms = Permission.objects.create(codename='add_admission', name='Can add Admission', content_type=content_type)
		user = UserProfile.objects.get(username='pije')
		group = Group.objects.get(name='Staff')
#		group.permissions.add(perms)
		user.groups.add(group)
#		group = Group.objects.get(name='')
#		group = Group.objects.create(name='Staff')

#		for p in perms:
#			group.permissions.add(p)

#		gGroupAdmins = Group(name='Staff')
#		gGroupAdmins.save()

#		g = Group.objects.get(name='Staff')
#		g.save()
#		users = User.objects.all()
#		for u in users:
#			g.user_set.add(u)
#		group, created = Group.objects.get_or_create(name='Staff')
#		group.save()

#		for group in GROUPS:
##		for group_name in GROUPS_PERMISSIONS:
#			new_group, created = Group.objects.get_or_create(name=group)
##			group, created = Group.objects.get_or_create(name=group_name)

#			for model in MODELS:
##			for model_cls in GROUPS_PERMISSIONS[group_name]:

#				for permission in PERMISSIONS:
##				for perm_index, perm_name in enumerate(GROUPS_PERMISSIONS[group_name][model_cls]):
#					name = 'Can {} {}'.format(permission, model)
##					codename = perm_name + "_" + model_cls._meta.model_name
#					print("Creating {}".format(name))
##					print("Creating {}".format(codename))

##					try:
#						model_add_perm = Permission.objects.get(name=name)
##						perm = Permission.objects.get(codename=codename)
##						group.permissions.add(perm)
##						self.stdout.write("Adding " + codename + " to group " + group.__str__())
##					except Permission.DoesNotExist:
#						logging.warning("Permission not found with name '{}'.".format(name))
##						self.stdout.write(codename + " not found")
#						continue

#					new_group.permissions.add(model_add_perm)

#		print("Created default group and permissions.")
#		testgroup = Group()
#		testgroup.name = 'testgroup'
#		testgroup, created = Group.objects.get_or_create(name='Staff')
#		testgroup.save()
#		ct = ContentType.objects.get_for_model(Admission)
#		permission = Permission.objects.create(codename='can_add_project', name='Can add project', content_type=ct)
#		new_group.permissions.add(permission)

#		if verbosity>0:
#			print("Initialising data post_syncdb")
#		for group in volunteer_group_permissions:
#			role, created = Group.objects.get_or_create(name=group)
#			if verbosity>1 and created:
#				print('Creating group', group)
#			for perm in myappname_group_permissions[group]: 
#				role.permissions.add(Permission.objects.get(codename=perm))
#				if verbosity>1:
#					print('Permitting', group, 'to', perm)
#			role.save()

#signals.post_syncdb.connect(create_user_groups, sender=UserProfile, dispatch_uid='accounts.userprofile.create_user_groups')