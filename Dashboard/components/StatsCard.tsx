"use client";

import { FC, useEffect, useState } from "react";
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "./ui/card";
import { Separator } from "./ui/separator";
import { toast } from "sonner";
import Loading from "./Loading";

interface StatsCardProps {}

const StatsCard: FC<StatsCardProps> = ({}) => {
  const [statsData, setStatsData] = useState(null);

  const toastMessage = (title: string, message: string, log: string) => {
    toast(title, {
      description: message,
      action: {
        label: "Dismiss",
        onClick: () => console.log(log),
      },
    });
  };

  const fetchData = async () => {
    try {
      const statsResponse = await fetch(process.env.NEXT_PUBLIC_STATS_URL!);
      const statsResult = await statsResponse.json();

      toastMessage(
        "Successfully Fetched Data",
        "Fetched data from Stats endpoint.",
        "Toast Dismissed"
      );

      statsResult["last_updated"] = statsResult["last_updated"]
        .split("T")
        .join(" ")
        .slice(0, -8);
      
      setStatsData(statsResult);
    } catch (error) {
      toastMessage(
        "Unable to Fetch Data",
        "There was an error fetching new data.",
        String(error)
      );
    }
  };

  useEffect(() => {
    const interval = setInterval(() => {
      fetchData();
    }, +process.env.NEXT_PUBLIC_FREQUENCY!);

    return () => {
      clearInterval(interval);
    };
  }, []);

  return (
    <>
      <Card className="bg-neutral-900 text-white mb-4 p-6">
        <CardHeader className="text-center">
          <CardTitle className="text-3xl">Latest Statistics</CardTitle>
        </CardHeader>
        {statsData === null ? (
          <Loading />
        ) : (
          <>
            <div className="flex gap-10">
              <CardContent className="flex flex-col gap-5">
                <div>
                  <h3 className="text-lg font-semibold">
                    Gun Stat Event Count
                  </h3>
                  <Separator className="mb-2" />
                  <p className="text-neutral-300">
                    {statsData["num_gun_stat_events"]}
                  </p>
                </div>
                <div>
                  <h3 className="text-lg font-semibold">Bullet Shot Count</h3>
                  <Separator className="mb-2" />
                  <p className="text-neutral-300">
                    {statsData["bullet_shot_count"]}
                  </p>
                </div>
                <div>
                  <h3 className="text-lg font-semibold">Head Shot Count</h3>
                  <Separator className="mb-2" />
                  <p className="text-neutral-300">
                    {statsData["head_shot_count"]}
                  </p>
                </div>
              </CardContent>

              <CardContent className="flex flex-col gap-5">
                <div>
                  <h3 className="text-lg font-semibold">
                    Purchase History Event Count
                  </h3>
                  <Separator className="mb-2" />
                  <p className="text-neutral-300">
                    {statsData["num_purchase_history_events"]}
                  </p>
                </div>
                <div>
                  <h3 className="text-lg font-semibold">Total Revenue</h3>
                  <Separator className="mb-2" />
                  <p className="text-neutral-300">
                    {statsData["total_revenue"]}
                  </p>
                </div>
              </CardContent>
            </div>

            <CardFooter className="justify-center text-neutral-400">
              <p>Last Updated: {statsData["last_updated"]}</p>
            </CardFooter>
          </>
        )}
      </Card>
    </>
  );
};

export default StatsCard;
