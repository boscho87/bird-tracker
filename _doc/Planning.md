# Idea

- [ ] Capture Sequences, when movement is detected
- [ ] Check if the Species is already in the Database
- [ ] Store the Sequence in the Database
- [x] Store the Sequence if the image is not recognized to learn new Species
  [ ]Let the User help to Learn the Species VIA WebUI
- [ ] Notify the User if a new Sequence is captured
- [ ] Show the Sequences in the WebUI


```plantuml
class VideoSequence {
  - video_path: str
  - time: int
}

class ImageSequence {
  - images: list[Image]
  - time: int
}

class Subject {
  - slug: str
  - name: str
  - id: int
}

class Event {
  - time: int
  - subject: Subject
}

class Match {
  - video_sequence: VideoSequence
  - subject: Subject
}

class Image {
  - image_path: str
  - time: int
}
```



