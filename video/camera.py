#!/usr/bin/python

import pygst
pygst.require("0.10")
import gst
#import pygtk
#import gtk


#gst-launch --gst-debug-level=2  v4l2src ! videorate  ! video/x-raw-yuv, width=320, height=240  ! theoraenc drop-frames=false ! oggmux ! queue !  tcpserversink port=5000


class Main:
    def __init__(self):
        self.pipeline = gst.Pipeline("pipeline")

        self.videosrc = gst.element_factory_make("v4l2src", "v4l2")
        #self.videosrc = gst.element_factory_make("videotestsrc", "v4l2")
        self.vfilter = gst.element_factory_make("capsfilter", "vfilter")
        self.vfilter.set_property('caps',gst.caps_from_string('video/x-raw-yuv, width=320, height=240'))

        self.color = gst.element_factory_make("ffmpegcolorspace",color)
        self.enc = gst.element_factory_make("theoraenc","enc")
        self.enc.set_property('drop-frames',False)
        
        self.mux = gst.element_factory_make("oggmux","mux")

        self.queue = gst.element_factory_make("queue","buffer")
        
class Main:
    def __init__(self):
        self.pipeline = gst.Pipeline("pipeline")

        self.videosrc = gst.element_factory_make("v4l2src", "v4l2")
        #self.videosrc = gst.element_factory_make("videotestsrc", "v4l2")
        self.vfilter = gst.element_factory_make("capsfilter", "vfilter")
        self.vfilter.set_property('caps',gst.caps_from_string('video/x-raw-yuv, width=320, height=240'))

        self.color = gst.element_factory_make("ffmpegcolorspace",color)
        self.enc = gst.element_factory_make("theoraenc","enc")
        self.enc.set_property('drop-frames',False)
        
        self.mux = gst.element_factory_make("oggmux","mux")

        self.queue = gst.element_factory_make("queue","buffer")
        
        self.tcpsink = gst.element_factory_make("tcpserversink","sink")
        self.tcpsink.set_property("host", "localhost")
        self.tcpsink.set_property("port", 5000)
        
        self.pipeline.add_many(self.videosrc, self.vfilter,self.color,  self.enc, self.mux, self.queue, self.tcpsink)
        gst.element_link_many(self.videosrc, self.vfilter,self.color,  self.enc, self.mux, self.queue, self.tcpsink)

        self.pipeline.set_state(gst.STATE_PLAYING)
    def pause(self):
        self.pipeline.set_state(gst.STATE_PAUSED)

#start=Main()
#gtk.main()
        self.tcpsink = gst.element_factory_make("tcpserversink","sink")
        self.tcpsink.set_property("host", "localhost")
        self.tcpsink.set_property("port", 5000)
        
        self.pipeline.add_many(self.videosrc, self.vfilter,self.color,  self.enc, self.mux, self.queue, self.tcpsink)
        gst.element_link_many(self.videosrc, self.vfilter,self.color,  self.enc, self.mux, self.queue, self.tcpsink)

        self.pipeline.set_state(gst.STATE_PLAYING)
    def pause(self):
        self.pipeline.set_state(gst.STATE_PAUSED)

#start=Main()
#gtk.main()