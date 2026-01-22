from utils import read_video, save_video
from trackers import PlayerTracker, BallTracker
from drawers import(PlayerTracksDrawer,BallTracksDrawer)
from team_assigner.team_assigner import TeamAssigner
from ball_acquisition import BallAquisitionDetector

def main():
    video_frames = read_video("input_videos/video_1.mp4")

    #Intialiaze tracker
    player_tracker = PlayerTracker("models/player_detector_model.pt")
    ball_tracker = BallTracker("models/ball_detector_model.pt")

    #Run Trackers
    player_tracks=player_tracker.get_object_tracks(
        video_frames,
        read_from_stub=True,stub_path="stubs/player_tracks.stubs.pkl"
    )
    ball_tracks=ball_tracker.get_object_tracks(
        video_frames,
        read_from_stub=True,stub_path="stubs/ball_tracks.stubs.pkl"
    )

    #Remove wrong ball Detections 
    ball_tracks=ball_tracker.remove_wrong_detections(ball_tracks)

    #Interpolate Ball Tracks
    ball_tracks=ball_tracker.interpolate_ball_positions(ball_tracks)

    #Assign Player Teams
    team_assigner=TeamAssigner()
    player_assignment=team_assigner.get_player_teams_across_frames(video_frames,player_tracks,read_from_stub=True,stub_path="stubs/player_assignment_stub.pkl")
    #Ball Aquisition
    ball_aquisition_detector=BallAquisitionDetector()
    ball_aquisition=ball_aquisition_detector.detect_ball_possession(player_tracks,ball_tracks)
    print(ball_aquisition)

    #Draw Output 
    #Intialize Drawer
    player_tracks_drawer=PlayerTracksDrawer()
    ball_tracks_drawer=BallTracksDrawer()

    #Draw Object Tracks
    output_video_frames=player_tracks_drawer.draw(video_frames,player_tracks,player_assignment)
    output_video_frames=ball_tracks_drawer.draw(output_video_frames,ball_tracks)
    
    #Save Video
    save_video(output_video_frames,"output_videos/output_video.avi")

if __name__ == "__main__":
    main()