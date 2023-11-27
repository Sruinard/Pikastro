"use client"; // top to the file
import React from "react";
import ChatWindow from "@/components/chatwindow";
import Layout from "@/components/layout";
import AIResponse from "@/components/AIResponse";
import { Button } from "@/components/ui/button";

const ChatPage = () => {
  // chatconverstaion contains responsecardsprops and inputprops
  const activeIndex = 2;

  const interactions = [
    {
      id: "1",
      ask: {
        message: "What is said about EVs in this article?",
      },
      context: {},
      response:
        "There are many benefits to EVs. One of which is that they are better for the environment.",
      responseType: "text",
    },
    {
      id: "2",
      ask: {
        message: "What metrics are shown about that?",
      },
      context: {},
      response: "They reduce carbon emissions by 50%.",
      responseType: "text",
    },
    {
      id: "3",
      ask: {
        message:
          "Give me an overview of what these 5 other articles are telling about this metric.",
      },
      context: {
        headers: ["Article", "Metric", "Sentiment"],
        rows: [
          ["Article 1", "50%", "Positive"],
          ["Article 2", "50%", "Positive"],
          ["Article 3", "50%", "Positive"],
          ["Article 4", "50%", "Positive"],
          ["Article 5", "50%", "Positive"],
        ],
      },
      response: "",
      responseType: "table",
    },
  ];

  return (
    <div>
      <Layout>
        <ChatWindow>
          <div className="flex w-full h-full items-center">
            <Button
              className="w-1/12"
              onClick={() => {
                setActiveIndex(activeIndex + 1);
              }}
            >
              Next
            </Button>
            {
              // loop through interactions and display the response cards and input
              <div className="flex-1 mx-10 h-1/2">
                {[interactions[activeIndex]].map((interaction) => {
                  return <AIResponse key={interaction.id} />;
                })}
              </div>
            }
          </div>
        </ChatWindow>
      </Layout>
    </div>
  );
};

export default ChatPage;
