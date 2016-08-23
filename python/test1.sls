#{% for k,v in pillar.get('product_role', {}).items() %}
#{{ k }}:
#    cmd.run:
#        - name: touch {{ k }}_{{ v[2] }}
#{% endfor %}

#xxxx:
#    cmd.run:
#        - name: echo {{ pillar['product_role']['E04'][0] }}
#        - template: jinja

{% for k,v in pillar.get('product_role', {}).items() %}
{{ k }}:
    cmd.run:
        - name: echo {{ k }}_{{ v[2] }}
{% endfor %}
