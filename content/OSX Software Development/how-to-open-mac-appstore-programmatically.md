Title: How to open Mac App Store Programmatically
Date: 2013-08-23 14:20
Category: OSX Software Development
Tags: cocoa, mac-app-store, objective-c, iTunes, NSWorkspace
Summary: How do you open your App Page in Mac App Store (desktop application) from your application
Slug: how-to-open-mac-app-store-programmatically
disqus_identifier: d50551b-how-to-open-mac-app-store-programmatically

Mac App Store is accessed using `macappstore` URL scheme. Your URL should follow this pattern:

    :::bash
    macappstore://itunes.apple.com/app/id[APP_ID]?mt=12

Replace `[APP_ID]` with your app's track id.

## How to find Track ID of any app

You can easily get track ID from URL of the application at App Store. For example, URL of Mac App Store page for Jump Desktop is 

    :::bash
    https://itunes.apple.com/ca/app/jump-desktop-remote-desktop/id524141863?mt=12

Number between `id` and `?` is the required ID which in this case is `524141863`.

Lets test it. Replace `[APP_ID]` with `524141863` in the `macappstore://` URL given above. Then open the URL from Terminal

    :::bash
    open macappstore://itunes.apple.com/app/id524141863?mt=12

This should open Mac App Store desktop application to Jump Desktop page.

## How to open Mac App Store from inside your Application

Now that we know the required URL scheme and track ID, opening iTunes page in Mac App Store is pretty simple. See the following code snippet.

    #!objective-c
    NSString *track_id = @"524141863";
    NSString *app_url_str = [NSString stringWithFormat:
        @"macappstore://itunes.apple.com/app/id%@?mt=12",
        track_id];
    // Create NSURL to pass it to NSWorkspace
    NSURL *app_url = [NSURL URLWithString:app_url_str];
    // Open URL
    [[NSWorkspace sharedWorkspace] openURL:app_url];
    
You just need to the pass `openURL:` message with correctly formed URL to `[NSWorkspace sharedWorkspace]` object.
