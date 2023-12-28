# AppVerse

A universe for apps.

AppVerse is a multi-platform app store built using Python, Django and Django REST Framework. It allows users to discover and install apps.


## Available API Endpoints

Here is a list of available API endpoints.

- Apps:
  1. `/apps`, methods: `GET` lists the apps, `POST` creates an app. 
  2. `/apps/{appId}`, methods: `GET` retrieves an app, `PUT` and `PATCH` update an app, `DELETE` deletes an app.
  3. `/apps/{appId}/icon`, methods: `GET` serves the app icon.
  4. `/apps/{appId}/cover`, methods: `GET` serves the app cover image.
  5. `/apps/{appId}/screenshots` methods: `GET` lists screenshots of an app, `POST` creates a screenshot for an app.
  6. `/apps/{appId}/screenshots/{screenshotId}` methods: `GET` retrieves a screenshot of an app, `PUT` and `PATCH` update a screenshot, `DELETE` deletes a screenshot.
  7. `/apps/{appId}/platforms` methods: `GET` lists platforms of an app, `POST` creates a release of an app for a specific platform.
  8. `/apps/{appId}/platforms/{platformId}` methods: `GET` retrieves an app release for a platform, `PUT` and `PATCH` update an app release for a platform, `DELETE` deletes an app release for a platform.
  9. `/apps/{appId}/reports` methods: `GET` lists reports of an app, `POST` creates a report for an app.
  10. `/apps/{appId}/reports/{reportId}` methods: `GET` retrieves a report of an app, `PUT` and `PATCH` update a report, `DELETE` deletes a report.
  11. `/apps/{appId}/reviews` methods: `GET` lists reviews of an app, `POST` creates a review for an app.
  12. `/apps/{appId}/reviews/{reviewId}` methods: `GET` retrieves a review of an app, `PUT` and `PATCH` update a review, `DELETE` deletes a review.

- Categories:
  1. `/categories`, methods: `GET` lists the categories, `POST` creates a category. 
  2. `/categories/{categoryId}`, methods: `GET` retrieves a category, `PUT` and `PATCH` update a category, `DELETE` deletes a category.
  3. `/categories/{categoryId}/apps`, methods: `GET` retrieves the apps of a category.
  4. `/categories/{categoryId}/apps/{appId}`, methods: `GET` retrieves the app.

- Devices:
  1. `/manufacturers`, methods: `GET` lists the manufacturers, `POST` creates a manufacturer.
  2. `/manufacturers/{manufacturersId}`, methods: `GET` retrieves a manufacturers, `PUT` and `PATCH` update a manufacturer, `DELETE` deletes a manufacturer.
  3. `/manufacturers/{manufacturersId}/models`, methods: `GET` retrieves the device models of a manufacturer, `POST` creates a new model.
  4. `/manufacturers/{manufacturersId}/models/{modelId}`, methods: `GET` retrieves the model, `PUT` and `PATCH` update a model, `DELETE` deletes a model.
  5. `/models`, methods: `GET` retrieves the device models, `POST` creates a new model.
  6. `/models/{modelId}`, methods: `GET` retrieves the model, `PUT` and `PATCH` update a model, `DELETE` deletes a model.
  7. `/devices`, methods: `GET` lists the devices.
  8. `/devices/{deviceId}`, methods: `GET` retrieves a device, `DELETE` deletes a device.