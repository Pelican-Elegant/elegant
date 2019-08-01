---
Title: Newsletter -- Add Mailchimp
Tags: marketing, network, subscriber
Date: 2013-08-27 23:20
comments: false
Slug: add-mailchimp
Category: Connecting With Your Readers
authors: Talha Mansoor
mailchimp_filter: off
freelists_filter: on
---

Elegant shows a form to subscribe to your newsletter, above the fold, in the right section of every article. Increased visibility is said to increase number of subscribers.

![Mailchimp subscriber
form]({static}/images/elegant-theme_subscribe-form.png)

You need to put your Mailchimp form action URL in `MAILCHIMP_FORM_ACTION` in your configuration file.

To customize user experience you can also define,

1. `EMAIL_SUBSCRIPTION_LABEL`,
1. `EMAIL_FIELD_PLACEHOLDER` and
1. `SUBSCRIBE_BUTTON_TITLE`

You can see Mailchimp Form in action in the sidebar. It's a working example. Enter your email address so that we can send you news of new Elegant releases in your inbox.

## Show Mailchimp Form by default

Just set `MAILCHIMP_FORM_ACTION` variable.

## Hide Mailchimp Form by default

Unset `MAILCHIMP_FORM_ACTION` variable.

This is the default setting.

## Hide Mailchimp Form by default. Show on Selected

1. Set `MAILCHIMP_FORM_ACTION`
1. Set `MAILCHIMP_FILTER` to `True`

This will hide Mailchimp form on all pages.

Now to show Mailchimp form on selected posts, in article metadata set

```yaml
mailchimp_filter: off
```

## Show Mailchimp Form by default. Hide on Selected

1. Set `MAILCHIMP_FORM_ACTION`
1. Remove `MAILCHIMP_FILTER` or set it to `False` which is its default value

This will hide Mailchimp form on all pages.

Now to hide Mailchimp form on selected posts, in article metadata set

```yaml
mailchimp_filter: on
```
