from cnnClassifier.entity.config_entity import TrainingConfig
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from sklearn.utils.class_weight import compute_class_weight
import numpy as np



class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            preprocessing_function=preprocess_input, # normalises to imagenet data distribution
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:2],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

        self.valid_generator = valid_datagen.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
                train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=15,          
                horizontal_flip=True,       
                vertical_flip=False,        
                width_shift_range=0.1,
                height_shift_range=0.1,
                zoom_range=0.1,
                brightness_range=(0.8, 1.2),  # brightness augmentation
                **datagenerator_kwargs
            )

        else:
            train_datagen = valid_datagen
        
        self.train_generator = train_datagen.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self):
        early_stop = EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True
        )

        checkpoint = ModelCheckpoint(
            self.config.trained_model_path,
            monitor='val_loss',
            save_best_only=True,
            verbose=1
        )

        reduce_lr = ReduceLROnPlateau(
            monitor='val_loss',   # or 'val_accuracy'
            factor=0.5,           # multiply LR by this
            patience=5,           # wait this many epochs
            min_lr=1e-6,
            verbose=1
        )

        #Errors on rare classes are penalised more than errors on common classes due to imbalance 

        class_weights = compute_class_weight(
            class_weight="balanced",
            classes=np.unique(self.train_generator.classes),
            y=self.train_generator.classes
        )

        class_weights = dict(enumerate(class_weights))

        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            class_weight=class_weights,
            callbacks=[reduce_lr, early_stop, checkpoint]
        )

       # self.save_model(
       #     path=self.config.trained_model_path,
       #     model=self.model
       # )
