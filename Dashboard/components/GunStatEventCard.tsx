import { FC } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Separator } from "./ui/separator";

interface GunStatEventCardProps {
  gsData: any,
  queryIndex: number
}

const GunStatEventCard: FC<GunStatEventCardProps> = ({ gsData, queryIndex }) => {
  const gunId = gsData['gun_id']
  const gameId = gsData['game_id']
  const userId = gsData['user_id']
  const numBulletsShot = gsData['num_bullets_shot']
  const numMissedShots = gsData['num_missed_shots']
  const numHeadShots = gsData['num_head_shots']
  const numBodyShots = gsData['num_body_shots']

  return (
    <>
      <Card className="bg-neutral-900 text-white p-7">
        <CardHeader>
          <CardTitle>Gun Stat Event</CardTitle>
          <CardDescription className="text-neutral-600">Fetched index value: {queryIndex}</CardDescription>
        </CardHeader>

        <CardContent>
          <h3 className="text-lg font-semibold">Gun ID</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{gunId}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">Game ID</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{gameId}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">User ID</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{userId}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">Number Bullets Shot</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{numBulletsShot}</p>
        </CardContent>
        
        <CardContent>
          <h3 className="text-lg font-semibold">Number Bullets Missed</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{numMissedShots}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">Number Head Shots</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{numHeadShots}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">Number Body Shots</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{numBodyShots}</p>
        </CardContent>
      </Card>
    </>
  );
};

export default GunStatEventCard;
