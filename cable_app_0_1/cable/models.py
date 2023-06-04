from django.db import models


class Machine(models.Model):
    name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Machine'


class Inductor(models.Model):
    name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Inductor'


class Cap(models.Model):
    name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cap'


class Clutch(models.Model):
    name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Clutch'


class Cable(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    cap = models.ForeignKey(Cap, on_delete=models.CASCADE)
    clutch = models.ForeignKey(Clutch, on_delete=models.CASCADE)
    inductor = models.ForeignKey(Inductor, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cable'
        ordering = ['-pk']
