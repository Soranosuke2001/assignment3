import { FC } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Separator } from "./ui/separator";

interface PurchaseEventCardProps {
  phData: any,
  queryIndex: number
}

const PurchaseEventCard: FC<PurchaseEventCardProps> = ({ phData, queryIndex }) => {
  const transactionId = phData['transaction_id']
  const itemId = phData['item_id']
  const userId = phData['user_id']
  const transactionDate = phData['transaction_date'].split('T').join(' ').slice(0, -1)
  const itemPrice = phData['item_price']

  return (
    <>
      <Card className="h-fit bg-neutral-900 text-white p-7">
        <CardHeader>
          <CardTitle className="text-white">Purchase Transaction Event</CardTitle>
          <CardDescription className="text-neutral-600">Fetched index value: {queryIndex}</CardDescription>
        </CardHeader>

        <CardContent>
          <h3 className="text-lg font-semibold">Transaction ID</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{transactionId}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">Item ID</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{itemId}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">User ID</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{userId}</p>
        </CardContent>

        <CardContent>
          <h3 className="text-lg font-semibold">Transaction Date</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{transactionDate}</p>
        </CardContent>
        
        <CardContent>
          <h3 className="text-lg font-semibold">Item Price</h3>
          <Separator className="mb-2" />
          <p className="text-neutral-300">{itemPrice}</p>
        </CardContent>
      </Card>
    </>
  );
};

export default PurchaseEventCard;
