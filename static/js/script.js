let now_playings = document.querySelectorAll('.now-playing');
let track_arts = document.querySelectorAll('.track-art');
let track_names = document.querySelectorAll('.track-name');
let track_artists = document.querySelectorAll('.track-artist');

let playpause_btns = document.querySelectorAll('.playpause-track');


let seek_sliders = document.querySelectorAll('.seek_slider');
let volume_sliders = document.querySelectorAll('.volume_slider');
let curr_times = document.querySelectorAll('.current-time');
let total_durations = document.querySelectorAll('.total-duration');
let wave = document.getElementById('wave');
let curr_tracks = document.querySelectorAll('audio');

let track_index = 0;
let isPlaying = false;
let isRandom = false;
let updateTimer;





function reset(){
    curr_times,total_durations,seek_sliders.forEach((curr_time,total_duration,seek_slider)=>{
        curr_time.textContent = "00:00";
        total_duration.textContent = "00:00";
        seek_slider.value = 0;
    })

}

function playpauseTrack(){
    isPlaying ? pauseTrack() : playTrack();
}
function playTrack(){
    curr_tracks.forEach((curr_track)=>{
        curr_track.play();
    })
    track_arts.forEach((track_art)=>{
        isPlaying = true;
        track_art.classList.add('rotate');
        wave.classList.add('loader');
        playpause_btns.forEach(playpause_btn=>{
            playpause_btn.innerHTML = '<i class="fa fa-pause-circle fa-5x"></i>';
        })
    })

}
function pauseTrack(){
    curr_tracks.forEach((curr_track)=>{
        curr_track.pause();
    })
    track_arts.forEach((track_art)=>{
    isPlaying = false;
    track_art.classList.remove('rotate');
    wave.classList.remove('loader');
    playpause_btns.forEach(playpause_btn=>{
        playpause_btn.innerHTML = '<i class="fa fa-play-circle fa-5x"></i>';
    })
    })
}

function seekTo(){
    curr_tracks,seek_sliders.forEach((curr_track,seek_slider)=>{
        let seekto = curr_track.duration * (seek_slider.value / 100);
        curr_track.currentTime = seekto;
    })

}
function setVolume(){
    curr_tracks,volume_sliders.forEach((curr_track,volume_slider)=>{
        curr_track.volume = volume_slider.value / 100;
    })

}
function setUpdate(){
    curr_tracks,curr_times,total_durations,seek_sliders.forEach((curr_track,curr_time,total_duration,seek_slider)=>{
        let seekPosition = 0;
        if(!isNaN(curr_track.duration)){
            seekPosition = curr_track.currentTime * (100 / curr_track.duration);
            seek_slider.value = seekPosition;
    
            let currentMinutes = Math.floor(curr_track.currentTime / 60);
            let currentSeconds = Math.floor(curr_track.currentTime - currentMinutes * 60);
            let durationMinutes = Math.floor(curr_track.duration / 60);
            let durationSeconds = Math.floor(curr_track.duration - durationMinutes * 60);
    
            if(currentSeconds < 10) {currentSeconds = "0" + currentSeconds; }
            if(durationSeconds < 10) { durationSeconds = "0" + durationSeconds; }
            if(currentMinutes < 10) {currentMinutes = "0" + currentMinutes; }
            if(durationMinutes < 10) { durationMinutes = "0" + durationMinutes; }
    
            curr_time.textContent = currentMinutes + ":" + currentSeconds;
            total_duration.textContent = durationMinutes + ":" + durationMinutes;
        }
    })

}