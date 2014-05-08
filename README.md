Base abstract Model for processing Django model's fields with [ALS typograf](http://www.artlebedev.ru/tools/typograf/webservice/).

	from django.db import models
	from typograf_model import TypoModel

	class SomeModel(TypoModel):
		name = models.CharField(max_length=255)
		text = = models.TextField()
		...
		
		_typo_fields = ['name',]
    	_typo_fields_para = ['text',]

Values of ​​listed fields will be processed when the model is saved