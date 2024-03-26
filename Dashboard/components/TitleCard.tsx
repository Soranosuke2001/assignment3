import { FC } from "react";
import { Card, CardDescription, CardHeader, CardTitle } from "./ui/card";
import Image from "next/image";

interface TitleCardProps {}

const TitleCard: FC<TitleCardProps> = ({}) => {
  return (
    <>
      <Card className="bg-neutral-900 mt-2">
        <CardHeader className="flex justify-center items-center">
          <Image src="/logo.png" alt="Video Game Logo" width={100} height={100}/>
          <CardTitle className="text-white text-5xl">Apex Gunners Statistics</CardTitle>
          <CardDescription>Learn all sorts of statistics based on the game Apex Gunners!</CardDescription>
        </CardHeader>
      </Card>
    </>
  );
};

export default TitleCard;
