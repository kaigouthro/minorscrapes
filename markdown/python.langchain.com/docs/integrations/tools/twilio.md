

Skip to main content

On this page

# Twilio

This notebook goes over how to use the Twilio API wrapper to send a message through SMS or Twilio Messaging Channels.

Twilio Messaging Channels facilitates integrations with 3rd party messaging apps and lets you send messages through WhatsApp Business Platform (GA), Facebook Messenger (Public Beta) and Google
Business Messages (Private Beta).

## Setup​

To use this tool you need to install the Python Twilio package `twilio`

```python




    # !pip install twilio



```


You'll also need to set up a Twilio account and get your credentials. You'll need your Account String Identifier (SID) and your Auth Token. You'll also need a number to send messages from.

You can either pass these in to the TwilioAPIWrapper as named parameters `account_sid`, `auth_token`, `from_number`, or you can set the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`,
`TWILIO_FROM_NUMBER`.

## Sending an SMS​

```python




    from langchain.utilities.twilio import TwilioAPIWrapper



```


```python




    twilio = TwilioAPIWrapper(
        #     account_sid="foo",
        #     auth_token="bar",
        #     from_number="baz,"
    )



```


```python




    twilio.run("hello world", "+16162904619")



```


## Sending a WhatsApp Message​

You'll need to link your WhatsApp Business Account with Twilio. You'll also need to make sure that the number to send messages from is configured as a WhatsApp Enabled Sender on Twilio and registered
with WhatsApp.

```python




    from langchain.utilities.twilio import TwilioAPIWrapper



```


```python




    twilio = TwilioAPIWrapper(
        #     account_sid="foo",
        #     auth_token="bar",
        #     from_number="whatsapp: baz,"
    )



```


```python




    twilio.run("hello world", "whatsapp: +16162904619")



```
