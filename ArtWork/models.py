from django.db import models


SGChoices = [('1', '1'), ('2', '2'), ('3', '3')]

SeasonChoices = [('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn(Fall)', 'Autumn(Fall)'), ('Winter', 'Winter'), ('NA', 'NA')]

MonthChoices = [('jan', 'jan'), ('feb', 'feb'), ('mar', 'mar'), ('apr', 'apr'), ('may', 'may'), ('jun', 'jun'), 
                ('jul', 'jul'), ('aug', 'aug'), ('sep', 'sep'), ('oct', 'oct'), ('nov', 'nov'), ('dec', 'dec'), ('NA', 'NA')]

DayChoices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), 
              ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), 
              ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), 
              ('29', '29'), ('30', '30'), ('31', '31'), ('NA', 'NA')]

OrientationChoices = [('Inside', 'Inside'), ('Outside', 'Outside'), ('NA', 'NA')]

OriginalityChoices = [('Original', 'Original'), ('Copy', 'Copy'), ('NA', 'NA')]

OrganicChoices = [('organic', 'organic'), ('synthetic', 'synthetic'), ('NA', 'NA')]



class Artist(models.Model):
    ArtistName = models.CharField(max_length=150, blank=True, null=True)
    # slug = models.SlugField()
    Nationality = models.CharField(max_length=150, blank=True, null=True)
    DateOfBirth = models.DateField()
    DateOfDeath = models.DateField()
    PrimaryMedium = models.CharField(max_length=150, blank=True, null=True)
    Education = models.CharField(max_length=50, blank=True, null=True)
    AwardsExhibitions = models.CharField(max_length=150, blank=True, null=True)
    # Movement = models.ManyToManyField(Movement)

    class Meta:
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.ArtistName

class Manufacture(models.Model):
     # slug = models.SlugField()
    CreationYear = models.IntegerField(blank=True, null=True)
    CreationMonth = models.CharField(max_length=3, choices=MonthChoices, blank=True, null=True)
    CreationDay = models.CharField(max_length=2, choices=DayChoices, blank=True, null=True)
    PlaceofManufacture = models.CharField(max_length=250, blank=True, null=True)
    SeasonofManufacture = models.CharField(max_length=20, choices=SeasonChoices, blank=True, null=True)
    Orientation = models.CharField(max_length=10, choices=OrientationChoices, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Manufacture"

    def __str__(self):
        return self.PlaceofManufacture
    

class Image(models.Model):
    F_Number = models.IntegerField(blank=True, null=True)
    InventoryNr = models.CharField(max_length=150, blank=True, null=True)
    ImageSource = models.URLField(blank=True, null=True)
    Remark = models.TextField(blank=True, null=True)
    image_1 = models.ImageField(default='default.jpg', blank=True, null=True)
    image_2 = models.ImageField(default='default.jpg', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return str(self.F_Number)



class pigment(models.Model):
    ColorIndex = models.CharField(max_length=50, blank=True, null=True)
    subgroup = models.CharField(max_length=50, blank=True, null=True)
    Name = models.CharField(max_length=150, blank=True, null=True)
    OrganicChoices = models.CharField(max_length=10, choices=OrganicChoices, blank=True, null=True)
    ASTM_Rating = models.CharField(max_length=10, blank=True, null=True)
    Remarks = models.TextField(blank=True, null=True)
    UsedBy = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    Found_In = models.CharField(max_length=250, blank=True, null=True)
    Source = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Pigments"

    def __str__(self):
        return self.Name



class SupportType(models.Model):
    Type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Types"

    def __str__(self):
        return self.Type

class Movement(models.Model):
    movement = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Movements"

    def __str__(self):
        return self.movement


class Ground(models.Model):
    ground = models.CharField(max_length=150, blank=True, null=True)
    underlayer = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Grounds"

    def __str__(self):
        return self.ground


class Technique(models.Model):
    technique = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Techniques"

    def __str__(self):
        return self.technique


class Brushshape(models.Model):
    brushshape = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = "BrushShapes"

    def __str__(self):
        return self.brushshape

class Underdrawingmaterial(models.Model):
    underdrawingmaterial = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = "UnderdrawingMaterials"

    def __str__(self):
        return self.underdrawingmaterial


class Finish(models.Model):
    finish = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Finish"

    def __str__(self):
        return self.finish

class Artwork(models.Model):
    Title = models.CharField(max_length=150, blank=True, null=True)
    Title_en = models.CharField(max_length=150, blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)    
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    Category = models.CharField(max_length=150, blank=True, null=True)
    Manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, blank=True, null=True)
    Currentlocation = models.CharField(max_length=150, blank=True, null=True)
    Currentowner = models.CharField(max_length=150, blank=True, null=True)
    Dimension = models.CharField(max_length=150, blank=True, null=True)
    OriginalOrCopy = models.CharField(max_length=150, choices=OriginalityChoices, blank=True, null=True)
    Seies = models.CharField(max_length=150, blank=True, null=True)
    SupportType = models.ForeignKey(SupportType, on_delete=models.CASCADE, blank=True, null=True)
    Movement = models.ForeignKey(Movement, on_delete=models.CASCADE, blank=True, null=True)
    DecayStatus = models.IntegerField(blank=True, null=True)
    Technique = models.ForeignKey(Technique, on_delete=models.CASCADE, blank=True, null=True)
    Ground = models.ForeignKey(Ground, on_delete=models.CASCADE, blank=True, null=True)
    Brushshape = models.ForeignKey(Brushshape, on_delete=models.CASCADE, blank=True, null=True)
    Underdrawingmaterial = models.ForeignKey(Underdrawingmaterial, on_delete=models.CASCADE, blank=True, null=True)
    Finish = models.ForeignKey(Finish, on_delete=models.CASCADE, blank=True, null=True)
    Pigment = models.ManyToManyField(pigment, blank=True)  
    Description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Artworks"

    def __str__(self):
        return self.Title
    

