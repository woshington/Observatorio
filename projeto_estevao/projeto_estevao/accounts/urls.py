from django.urls import path, include
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import views as auth_views
# from .forms import PasswordResetForm
from .views import *

app_name='accounts'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
	# Recovery Password
  #   path(
		# 'change-password/',
		# 	auth_views.PasswordChangeView.as_view(
		# 		template_name='accounts/password_change.html',
		# 		success_url=reverse_lazy('accounts:password_reset_complete')
		# 	),
		# name='password_change'),
  #   #path('change-password-done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
  #   path(
		# 'reset-passowrd/',
		# 	auth_views.PasswordResetView.as_view(
	 #            from_email='Patrimônio: <nrdesales@gmail.com>',
	 #            template_name='accounts/password_reset.html',
	 #            html_email_template_name='accounts/password_reset_email.html',
	 #            email_template_name='accounts/password_reset_email.txt',
		# 		form_class = PasswordResetForm,
	 #            success_url=reverse_lazy('accounts:password_reset_done'),
	 #        ),
		# name='password_reset'),
  #   path(
		# 'password-reset-done/',
		# 	auth_views.PasswordResetDoneView.as_view(
		# 		template_name= 'accounts/password_reset_done.html'
		# 	),
		# name='password_reset_done'),
  #   path(
		# 'reset/<uidb64>/<token>/',
  #       	auth_views.PasswordResetConfirmView.as_view(
		# 		template_name='accounts/password_reset_confirm.html',
		# 		success_url=reverse_lazy('accounts:password_reset_complete')
		# 	),
		# name='password_reset_confirm'),
  #   path(
		# 'recovery-done/',
		# 	auth_views.PasswordResetCompleteView.as_view(
		# 		template_name= 'accounts/password_reset_complete.html'
		# 	),
		# name='password_reset_complete'),
	# User edit profile
	# path('user/edit-profile/<int:pk>/', permission_required('accounts:user_profile_edit', raise_exception=True)(UserProfileEdit.as_view()), name='user_profile_edit'),
	# User
	path('list/', permission_required('accounts:user_list', raise_exception=True)(UserList.as_view()), name='user_list'),
	path('add/', permission_required('accounts:user_add', raise_exception=True)(UserCreate.as_view()), name='user_add'),
	path('edit/<int:pk>/', permission_required('accounts:user_edit', raise_exception=True)(UserUpdate.as_view()), name='user_edit'),
	path('details/<int:pk>/', permission_required('accounts:user_details', raise_exception=True)(UserDetail.as_view()), name='user_details'),
	path('<int:pk>/delete/', (user_delete), name='user_delete'),

	
]
