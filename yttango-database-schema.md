### Database Design (Postgres Schema)

(This is a preliminary schema based on the functional specification and may evolve during development)

| Table Name   | Column Name             | Data Type     | Primary Key | Foreign Key         | Notes                                                                                                |
| ------------ | ----------------------- | ------------- | ----------- | ------------------- | ---------------------------------------------------------------------------------------------------- |
| **videos** | video_id                | VARCHAR (255) | Yes         |                     | YouTube video ID                                                                                     |
|              | title                   | TEXT          |             |                     |                                                                                                      |
|              | channel_name            | VARCHAR (255) |             |                     |                                                                                                      |
|              | channel_url             | TEXT          |             |                     |                                                                                                      |
|              | description             | TEXT          |             |                     |                                                                                                      |
|              | publication_date        | TIMESTAMP     |             |                     |                                                                                                      |
|              | length_seconds          | INTEGER       |             |                     |                                                                                                      |
|              | transcript              | TEXT          |             |                     | Cached transcript content                                                                            |
|              | summary                 | TEXT          |             |                     | AI-generated summary                                                                                 |
|              | tags                    | TEXT          |             |                     | Comma-separated list of tags                                                                          |
|              | subject_area            | VARCHAR (255) | No          | subjects.name       |                                                                                                      |
|              | date_added              | TIMESTAMP     |             |                     | Timestamp when the video was added to Yttango                                                        |
| **channels** | channel_url             | TEXT          | Yes         |                     | YouTube channel URL                                                                                  |
|              | channel_name            | VARCHAR (255) |             |                     |                                                                                                      |
|              | description             | TEXT          |             |                     | Short description of the channel                                                                     |
|              | last_synced             | TIMESTAMP     |             |                     | Date and time of the last successful sync                                                              |
|              | subject_area            | VARCHAR (255) | No          | subjects.name       |                                                                                                      |
| **playlists**| playlist_url            | TEXT          | Yes         |                     | YouTube playlist URL                                                                                 |
|              | playlist_name           | VARCHAR (255) |             |                     |                                                                                                      |
|              | creator                 | VARCHAR (255) |             |                     | Channel owner name                                                                                   |
|              | description             | TEXT          |             |                     | Editable playlist description                                                                        |
|              | last_synced             | TIMESTAMP     |             |                     | Date and time of the last successful sync                                                              |
|              | subject_area            | VARCHAR (255) | No          | subjects.name       |                                                                                                      |
| **subjects** | name                    | VARCHAR (255) | Yes         |                     | User-defined subject area names                                                                        |
|              | date_created            | TIMESTAMP     |             |                     | Timestamp when the subject area was created                                                            |
| **video_playlist_association** | video_id              | VARCHAR (255) | Yes         | videos.video_id     | Many-to-many relationship between videos and playlists (if we re-introduce playlist creation) |
|              | playlist_url            | TEXT          | Yes         | playlists.playlist_url |                                                                                                      |