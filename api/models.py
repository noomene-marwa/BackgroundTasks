from django.db import models

class BaseModel(models.Model):
    """
    Data required in every table is created in this model and inherited by below models.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(BaseModel):
    """
    User model stores all user related information.
    """

    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    user_name = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=True)
    password = models.CharField( max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
