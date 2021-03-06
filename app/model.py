from nba_api.stats.endpoints import commonplayerinfo, shotchartdetail


class GetInfo:
    @staticmethod
    def getPlayerInfo(playerid):
        data = commonplayerinfo.CommonPlayerInfo(player_id=playerid, timeout=10).get_dict()
        print("data = ", data)
        return data

    @staticmethod
    def getShot(playerid, teamid):
        data = shotchartdetail.ShotChartDetail(player_id=playerid, team_id=teamid,
                                               season_type_all_star="Regular Season", season_nullable="2015-16",
                                               context_measure_simple="FGM", timeout=10).get_dict()

        return data
