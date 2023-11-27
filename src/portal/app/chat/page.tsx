"use client"; // top to the file
import React from "react";
import ChatWindow from "@/components/chatwindow";
import Layout from "@/components/layout";
import AIResponse from "@/components/AIResponse";
import { Button } from "@/components/ui/button";
import UserInput from "@/components/UserInput";

const ChatPage = () => {
  // chatconverstaion contains responsecardsprops and inputprops
  const [activeIndex, setActiveIndex] = React.useState(0);

  return (
    <div>
      <Layout>
        <ChatWindow>
          <div className="flex w-full h-full items-center">
            <div className="flex flex-col flex-1 mx-10 justify-center items-center h-full">
              <div className="flex w-3/4 h-2/6">
                <div className="flex flex-col h-full justify-center space-y-2 m-2">
                  <Button
                    onClick={() => {
                      setActiveIndex(activeIndex - 1);
                    }}
                  >
                    Previous
                  </Button>
                  <Button
                    onClick={() => {
                      setActiveIndex(activeIndex + 1);
                    }}
                  >
                    Next
                  </Button>
                </div>
                <AIResponse key="1" />
              </div>
              <div className="m-10 w-3/4 h-1/6 shadow-black">
                <UserInput />
              </div>
            </div>
          </div>
        </ChatWindow>
      </Layout>
    </div>
  );
};

export default ChatPage;
