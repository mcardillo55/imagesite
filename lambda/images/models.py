from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    file = models.CharField(max_length=200)  # stores the filename, e.g. "ABggJRZyR.jpg"
    img_hash = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    # Store as a raw integer to avoid depending on django.contrib.auth.
    # The original column is "uploaded_by_id" (FK to auth_user).
    uploaded_by_id = models.IntegerField(blank=True, null=True, db_column="uploaded_by_id")
    view_count = models.IntegerField(default=0)

    class Meta:
        db_table = "images_image"
        managed = False
