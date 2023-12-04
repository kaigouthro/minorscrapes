

Skip to main content

On this page

# Google Translate

Google Translate is a multilingual neural machine translation service developed by Google to translate text, documents and websites from one language into another.

The `GoogleTranslateTransformer` allows you to translate text and HTML with the Google Cloud Translation API.

To use it, you should have the `google-cloud-translate` python package installed, and a Google Cloud project with the Translation API enabled. This transformer uses the Advanced edition (v3).

  * Google Neural Machine Translation
  * A Neural Network for Machine Translation, at Production Scale

```python




    pip install google-cloud-translate



```


```python




    from langchain.document_transformers import GoogleTranslateTransformer
    from langchain.schema import Document



```


## Input​

This is the document we'll translate

```python




    sample_text = """[Generated with Google Bard]
    Subject: Key Business Process Updates

    Date: Friday, 27 October 2023

    Dear team,

    I am writing to provide an update on some of our key business processes.

    Sales process

    We have recently implemented a new sales process that is designed to help us close more deals and grow our revenue. The new process includes a more rigorous qualification process, a more streamlined proposal process, and a more effective customer relationship management (CRM) system.

    Marketing process

    We have also revamped our marketing process to focus on creating more targeted and engaging content. We are also using more social media and paid advertising to reach a wider audience.

    Customer service process

    We have also made some improvements to our customer service process. We have implemented a new customer support system that makes it easier for customers to get help with their problems. We have also hired more customer support representatives to reduce wait times.

    Overall, we are very pleased with the progress we have made on improving our key business processes. We believe that these changes will help us to achieve our goals of growing our business and providing our customers with the best possible experience.

    If you have any questions or feedback about any of these changes, please feel free to contact me directly.

    Thank you,

    Lewis Cymbal
    CEO, Cymbal Bank
    """



```


When initializing the `GoogleTranslateTransformer`, you can include the following parameters to configure the requests.

  * `project_id`: Google Cloud Project ID.
  * `location`: (Optional) Translate model location.
    * Default: `global`
  * `model_id`: (Optional) Translate model ID to use.
  * `glossary_id`: (Optional) Translate glossary ID to use.
  * `api_endpoint`: (Optional) Regional endpoint to use.

```python




    documents = [Document(page_content=sample_text)]
    translator = GoogleTranslateTransformer(project_id="<YOUR_PROJECT_ID>")



```


## Output​

After translating a document, the result will be returned as a new document with the `page_content` translated into the target language.

You can provide the following keyword parameters to the `transform_documents()` method:

  * `target_language_code`: ISO 639 language code of the output document.
    * For supported languages, refer to Language support.
  * `source_language_code`: (Optional) ISO 639 language code of the input document.
    * If not provided, language will be auto-detected.
  * `mime_type`: (Optional) Media Type of the input text.
    * Options: `text/plain` (Default), `text/html`.

```python




    translated_documents = translator.transform_documents(
        documents, target_language_code="es"
    )



```


```python




    for doc in translated_documents:
        print(doc.metadata)
        print(doc.page_content)



```


```python




        {'model': '', 'detected_language_code': 'en'}
        [Generado con Google Bard]
        Asunto: Actualizaciones clave de procesos comerciales

        Fecha: viernes 27 de octubre de 2023

        Estimado equipo,

        Le escribo para brindarle una actualización sobre algunos de nuestros procesos comerciales clave.

        Proceso de ventas

        Recientemente implementamos un nuevo proceso de ventas que está diseñado para ayudarnos a cerrar más acuerdos y aumentar nuestros ingresos. El nuevo proceso incluye un proceso de calificación más riguroso, un proceso de propuesta más simplificado y un sistema de gestión de relaciones con el cliente (CRM) más eficaz.

        Proceso de mercadeo

        También hemos renovado nuestro proceso de marketing para centrarnos en crear contenido más específico y atractivo. También estamos utilizando más redes sociales y publicidad paga para llegar a una audiencia más amplia.

        proceso de atención al cliente

        También hemos realizado algunas mejoras en nuestro proceso de atención al cliente. Hemos implementado un nuevo sistema de atención al cliente que facilita que los clientes obtengan ayuda con sus problemas. También hemos contratado más representantes de atención al cliente para reducir los tiempos de espera.

        En general, estamos muy satisfechos con el progreso que hemos logrado en la mejora de nuestros procesos comerciales clave. Creemos que estos cambios nos ayudarán a lograr nuestros objetivos de hacer crecer nuestro negocio y brindar a nuestros clientes la mejor experiencia posible.

        Si tiene alguna pregunta o comentario sobre cualquiera de estos cambios, no dude en ponerse en contacto conmigo directamente.

        Gracias,

        Platillo Lewis
        Director ejecutivo, banco de platillos




```
