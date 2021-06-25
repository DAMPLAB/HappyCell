<script>
import SVG from '@yapv/svg';

export default {
	functional: true,
	render (h, context) {
		const TrackComponent = SVG.circular.TrackComponent(h);
    return TrackComponent(context.props, context.children);
	}
}
</script>
