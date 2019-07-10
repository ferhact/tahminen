<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html> 
	
<style>
.mytable-textal{
	text-align:center;
    width:100%;
}
</style>
			<body>
				<h2>MGM_GDX Sıcaklık Tahmini</h2>
				<h3>[<xsl:value-of select="items/item/merkezde_gunderece[position() = 1]/kayit_tarih"/>] - [<xsl:value-of select="count(items/item/merkezde_gunderece)"/> Merkez]</h3>
				<table border="1">
					<tr bgcolor="#9acd32">
						<th style="text-align:left">ID</th>
						<th style="text-align:left">Merkez</th>
						<th style="text-align:left"><xsl:value-of select="items/item/merkezde_gunderece//gunderece/value[position() = 1]/gun"/></th>
						<th style="text-align:left"><xsl:value-of select="items/item/merkezde_gunderece//gunderece/value[position() = 2]/gun"/></th>
						<th style="text-align:left"><xsl:value-of select="items/item/merkezde_gunderece//gunderece/value[position() = 3]/gun"/></th>
						<th style="text-align:left"><xsl:value-of select="items/item/merkezde_gunderece//gunderece/value[position() = 4]/gun"/></th>
						<th style="text-align:left"><xsl:value-of select="items/item/merkezde_gunderece//gunderece/value[position() = 5]/gun"/></th>
						<th style="text-align:left">Kaynak</th> 

					</tr>
					<xsl:for-each select="items/item/merkezde_gunderece">
						<xsl:sort select="merkez_id" data-type="number"/>
						<tr>
							<td><xsl:value-of select="merkez_id"/></td>
							<td><xsl:value-of select="merkez_adi"/></td>
							<xsl:for-each select="gunderece/value">
								<td><div class="mytable-textal"><table text-align="center"><tr text-align="center"><td text-align="center"><xsl:value-of select="max_g"/>°</td></tr><tr><td><xsl:value-of select="max_gort"/>°</td></tr><tr><td>«----<xsl:value-of select="max"/>°----»</td></tr><tr><td><xsl:value-of select="min_gort"/>°</td></tr><tr><td><xsl:value-of select="min_g"/>°</td></tr></table></div></td>
							</xsl:for-each>
							<td>
								<a>
									<xsl:attribute name="href">
										<xsl:value-of select="kayit_url" />
									</xsl:attribute>url
								</a>
								(<xsl:value-of select="kayit_tarih" />)
							</td>

						</tr>
						</xsl:for-each>
					</table>
				</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>