import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

export default function UserInput() {
  return (
    <div className="grid w-full h-full gap-2">
      <Textarea
        className="shadow-lg border-2 border-black"
        placeholder="Type your message here."
      />
      <Button>Send message</Button>
    </div>
  );
}
