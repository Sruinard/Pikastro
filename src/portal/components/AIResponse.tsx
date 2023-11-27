import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

type ResponseType = "text" | "image" | "table";

interface TableResponseContent {
  headers: string[];
  data: any[];
}

interface TextResponseContent {
  text: string;
}

interface ImageResponseContent {
  url: string;
}

type ResponseContent =
  | TableResponseContent
  | TextResponseContent
  | ImageResponseContent;

interface Response {
  id: string;
  type: ResponseType;
  content: ResponseContent;
  created: Date;
}

interface AIResponseProps {
  context: string;
  responses: Response[];
}

const InteractionContext = ({ context }: { context: string }) => {
  return (
    <Accordion type="single" collapsible className="w-full">
      <AccordionItem value="item-1">
        <AccordionTrigger>user context</AccordionTrigger>
        <AccordionContent>{context}</AccordionContent>
      </AccordionItem>
    </Accordion>
  );
};

const TableResponse = ({ content }: { content: any }) => {
  return (
    <Table>
      <TableCaption>Table caption</TableCaption>
      <TableHead>
        <TableRow>
          {content.headers.map((header: string) => {
            return <TableHeader key={header}>{header}</TableHeader>;
          })}
        </TableRow>
      </TableHead>
      <TableBody>
        {content.data.map((row: any) => {
          return (
            <TableRow key={row[0]}>
              {row.map((cell: string) => {
                return <TableCell key={cell}>{cell}</TableCell>;
              })}
            </TableRow>
          );
        })}
      </TableBody>
    </Table>
  );
};

export default function AIResponse() {
  const interaction: AIResponseProps = {
    context: "How much is spend on food?",
    responses: [
      {
        id: "1",
        type: "table",
        content: {
          headers: ["Year", "Amount"],
          data: [
            ["2018", "$1000"],
            ["2019", "$2000"],
            ["2020", "$3000"],
          ],
        },
        created: new Date(),
      },
    ],
  };

  return (
    <Card className="flex flex-col w-full h-full shadow-black ">
      <CardHeader>
        <InteractionContext context={interaction.context} />
      </CardHeader>
      <CardContent>
        {interaction.responses.map((response: Response) => {
          return (
            <div key={response.id}>
              {response.type === "table" && (
                <TableResponse content={response.content} />
              )}
            </div>
          );
        })}
      </CardContent>
    </Card>
  );
}
