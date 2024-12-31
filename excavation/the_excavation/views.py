from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Excavation, Grave
from .serializers import ExcavationSerializer, GraveSerializer

def home(request):
    return HttpResponse( """
        <html>
            <head>
                <title>Welcome to the Excavation App</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; margin: 0; padding: 0; }
                    .container { width: 80%; margin: 50px auto; }
                    .header { text-align: center; }
                    .header h1 { color: #2d3e50; font-size: 36px; }
                    .intro { font-size: 18px; color: #555; line-height: 1.6; }
                    .call-to-action { background-color: #009688; color: white; padding: 15px 25px; border-radius: 5px; text-align: center; font-size: 20px; }
                    .cta-link { color: white; text-decoration: none; }
                    .cta-link:hover { text-decoration: underline; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Welcome to the Excavation App</h1>
                    </div>
                    <div class="intro">
                        <p>Welcome to the Excavation App. This platform is designed to support archaeologists in managing, documenting, and organizing their excavation data with precision and efficiency. Whether you are exploring ancient ruins or investigating valuable artifacts, this app provides the tools to ensure that your findings are thoroughly recorded and easily accessible.</p>
                        <p>The Excavation App enables you to:</p>
                        <ul>
                            <li><strong>Document Excavation Data</strong>: Record detailed information about your discoveries, such as pottery, bones, tools, jewelry, and more.</li>
                            <li><strong>Track Find Locations</strong>: Accurately log the east/north dimensions and depth of each finding to map its precise position within the excavation site.</li>
                            <li><strong>Manage Graves and Artifacts</strong>: Easily add descriptions and details regarding any graves or important artifacts you uncover.</li>
                            <li><strong>Collaborate Efficiently</strong>: Share data with your team, enabling collaborative input and real-time updates across the excavation project.</li>
                        </ul>
                        <p>All data is securely organized under each individual excavation project, allowing for streamlined documentation and easy access to important details.</p>
                        <p>We invite you to begin by exploring your current excavation projects and adding any new findings to ensure comprehensive record-keeping.</p>
                    </div>
                    <div class="call-to-action">
                        <a href="/the_excavation/" class="cta-link">View Excavation Projects</a>
                    </div>
                </div>
            </body>
        </html>
        """)

class ExcavationViewSet(viewsets.ModelViewSet):
    queryset = Excavation.objects.all()
    serializer_class = ExcavationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GraveViewSet(viewsets.ModelViewSet):
    queryset = Grave.objects.all()
    serializer_class = GraveSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        excavation_id = self.request.data.get('excavation_id')
        excavation = Excavation.objects.get(id=excavation_id)
        serializer.save(excavation=excavation)

