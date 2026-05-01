 class StreamingSong {
    String title;
    String artist;
    int duration;
    void play() {
        System.out.println("Playing song");
    }
    void printDetails() {
        System.out.println("This is " + title +
                " by " + artist);
    }
}
class StreamingSongTestDrive {
    public static void main(String[] args) {
        StreamingSong song = new StreamingSong();
        song.artist = "The Beatles";
        song.title = "Come Together";
        song.play();
        song.printDetails();
    }
}

 class DrumKit {
     boolean topHat = true;
     boolean snare = true;
     void playTopHat() {
         System.out.println("ding ding da-ding");
     }
     void playSnare() {
         System.out.println("bang bang ba-bang");
     }
 }
 class DrumKitTestDrive {
     public static void main(String[] args) {
         DrumKit d = new DrumKit();
         d.playSnare();
         d.snare = false;
         d.playTopHat();
         if (d.snare == true) {
             d.playSnare();
         }
     }
 }