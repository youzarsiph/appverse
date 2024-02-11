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

- Developers:

  1. `/developers`, methods: `GET` lists the developers, `POST` creates a developer.
  2. `/developers/{developerId}`, methods: `GET` retrieves a developer, `PUT` and `PATCH` update a developer, `DELETE` deletes a developer.
  3. `/developers/{developerId}/approve`, methods: `POST` approves a developer.
  4. `/developers/{developerId}/image`, methods: `GET` serves the image of a developer.
  5. `/developers/{developerId}/apps` methods: `GET` lists apps of a developer.
  6. `/developers/{developerId}/apps/{appId}` methods: `GET` retrieves an app of a developer.

- Installs:

  1. `/installs`, methods: `GET` lists the app installs.
  2. `/installs/{installId}`, methods: `GET` retrieves an app install.

- Orders:

  1. `/orders`, methods: `GET` lists the orders, `POST` creates an order.
  2. `/orders/{orderId}`, methods: `GET` retrieves an order, `PUT` and `PATCH` update an order, `DELETE` deletes an order.

- Permissions:

  1. `/permissions`, methods: `GET` lists the permissions, `POST` creates a permission.
  2. `/permissions/{permissionId}`, methods: `GET` retrieves a permission, `PUT` and `PATCH` update a permission, `DELETE` deletes a permission.

- Platforms:

  1. `/platforms`, methods: `GET` lists the platforms, `POST` creates a platform.
  2. `/platforms/{platformId}`, methods: `GET` retrieves a platform, `PUT` and `PATCH` update a platform, `DELETE` deletes a platform.
  3. `/platforms/{platformId}/apps` methods: `GET` lists apps of a platform.
  4. `/platforms/{platformId}/apps/{appId}` methods: `GET` retrieves a app of a platform.
  5. `/platforms/{platformId}/versions` methods: `GET` lists versions of a platform, `POST` creates a version.
  6. `/platforms/{platformId}/versions/{versionId}` methods: `GET` retrieves a version of a platform, `PUT` and `PATCH` update a version, `DELETE` deletes a version.
  7. `/versions`, methods: `GET` lists the versions, `POST` creates a version.
  8. `/versions/{versionId}`, methods: `GET` retrieves a version, `PUT` and `PATCH` update a version, `DELETE` deletes a version.

- Reports:

  1. `/reports`, methods: `GET` lists the reports, `POST` creates a report.
  2. `/reports/{reportId}`, methods: `GET` retrieves a report, `PUT` and `PATCH` update a report, `DELETE` deletes a report.

- Reviews:

  1. `/reviews`, methods: `GET` lists the reviews, `POST` creates a review.
  2. `/reviews/{reviewId}`, methods: `GET` retrieves a review, `PUT` and `PATCH` update a review, `DELETE` deletes a review.

- Screenshots:

  1. `/screenshots`, methods: `GET` lists the screenshots, `POST` creates a screenshot.
  2. `/screenshots/{screenshotId}`, methods: `GET` retrieves a screenshot, `PUT` and `PATCH` update a screenshot, `DELETE` deletes a screenshot.
  3. `/screenshots/{screenshotId}/image`, methods: `GET` serves the image of a screenshot.

- Tags:

  1. `/tags`, methods: `GET` lists the tags, `POST` creates a tag.
  2. `/tags/{tagId}`, methods: `GET` retrieves a tag, `PUT` and `PATCH` update a tag, `DELETE` deletes a tag.
  3. `/tags/{tagId}/apps` methods: `GET` lists apps of a tag.
  4. `/tags/{tagId}/apps/{appId}` methods: `GET` retrieves a app of a tag.

- Views:
  1. `/views`, methods: `GET` lists the app views, `POST` creates an app view.
  2. `/views/{viewId}`, methods: `GET` retrieves a view, `PUT` and `PATCH` update a view, `DELETE` deletes a view.
